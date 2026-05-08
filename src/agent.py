import json
import re
import logging
import os
from typing import List, Dict, Any

from agent_base import (
    BaseAgent, 
    AgentInput, 
    AgentOutput,
    UsageInfo,
    ACTION_CLICK,
    ACTION_SCROLL,
    ACTION_TYPE,
    ACTION_OPEN,
    ACTION_COMPLETE
)

# 兼容主办方环境
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

logger = logging.getLogger(__name__)


class Agent(BaseAgent):
    """
    终极护航版 Agent：修复了坐标变量输出、键名错误以及特定的视觉动作误判
    """

    def reset(self):
        """重置内部状态"""
        self.internal_history = []
        logger.info("--- 任务重置：开始新的测试用例 ---")

    def _build_system_prompt(self, instruction: str) -> str:
        return f"""你是一个顶尖的安卓手机 GUI 自动化代理。
【任务目标】：{instruction}

【核心交互铁律】：
1. 完结判定（极其重要）：当你点击了发送、提交、付款等终点按钮，或者观察到已到达目标结果页，必须立刻输出 ACTION 为 "COMPLETE"。
2. 搜索操作规范：如果指令要求“搜索”，你必须优先 CLICK 屏幕上的【搜索图标/放大镜/搜索框】，千万不要直接点击下方的推荐内容！等软键盘弹出后，再执行 TYPE 操作。
3. 动作白名单：
   - 第一步打开应用时，使用 OPEN。
   - 需要点击屏幕具体位置时，只能使用 CLICK。绝对不要在后续步骤使用 OPEN 来代替 CLICK！
4. 坐标系统：所有坐标必须是具体的整数数字，如 [500, 500]，绝对严禁在 JSON 中输出 [x, y] 这种代表变量的英文字母！坐标范围是 [0, 1000]。

【输出格式要求】：
你必须且只能输出一个合法的 JSON 块：
```json
{{
    "thought": "分析当前截图与任务的差距，回忆上一步，决定下一步",
    "action": "CLICK 或 TYPE 或 SCROLL 或 OPEN 或 COMPLETE",
    "parameters": {{
        "point": [500, 500],
        "text": "需要输入的具体文字",
        "start_point": [500, 800],
        "end_point": [500, 200],
        "app_name": "具体应用名称"
    }}
}}
"""

    def act(self, input_data: AgentInput) -> AgentOutput:
        """核心决策逻辑"""
        try:
            history_text = ""
            if input_data.history_actions:
                last_act = input_data.history_actions[-1]
                history_text = f"【提示】你上一步执行了: {last_act['action']}，参数为: {last_act['parameters']}。\n"
                if last_act['action'] == ACTION_TYPE:
                    history_text += "【注意】上一步已输入文字，请检查是否需要点击发送/搜索按钮，或者点击下拉联想词。尽量避免连续两次 TYPE。\n"
                elif last_act['action'] == ACTION_CLICK:
                    history_text += "【注意】如果上一步你点击的是输入框并且键盘已弹出，这一步请直接使用 TYPE 打字。如果不是，请根据需要继续操作。\n"

            messages = [
                {"role": "system", "content": self._build_system_prompt(input_data.instruction)},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": f"当前是第 {input_data.step_count} 步。\n{history_text}请观察截图并给出下一步。如果任务已实质完成，请直接输出 COMPLETE。"},
                        {"type": "image_url", "image_url": {"url": self._encode_image(input_data.current_image)}}
                    ]
                }
            ]

            response = self._call_api(messages, temperature=0.1)
            raw_content = response.choices[0].message.content
            logger.info(f"模型原始输出: {raw_content}")

            parsed_data = self._parse_json_robustly(raw_content)
            action = parsed_data.get("action", ACTION_COMPLETE).upper()
            params = parsed_data.get("parameters", {})
            if not isinstance(params, dict):
                params = {}

            # ==========================================
            # 官方参数严格对齐与异常修复区
            # ==========================================

            # 防止模型在非第一步时误把 CLICK 写成了 OPEN (修复腾讯视频用例)
            if action == ACTION_OPEN and input_data.step_count > 1 and "point" in params and "app_name" not in params:
                logger.warning("修正：在非第一步使用了 OPEN 并附带坐标，自动修正为 CLICK。")
                action = ACTION_CLICK

            if action == ACTION_OPEN:
                val = params.get("app_name") or params.get("app") or params.get("appName") or params.get("name") or ""
                # 修复去哪儿旅行少字的问题
                if "去哪" in val and "旅行" in val:
                    val = "去哪儿旅行"
                params = {"app_name": val}

            elif action == ACTION_TYPE:
                val = params.get("text") or params.get("content") or params.get("value") or ""
                params = {"text": val}

            elif action == ACTION_CLICK:
                if "point" not in params:
                    x, y = params.get("x"), params.get("y")
                    if x is not None and y is not None:
                        params["point"] = [x, y]

                if "point" in params:
                    pt = params["point"]
                    if isinstance(pt, list) and len(pt) >= 2:
                        if isinstance(pt[0], list):
                            pt = pt[0]
                        try:
                            # 强制转换为整型，防止模型输出字母 'x' 导致崩溃
                            params["point"] = [max(0, min(1000, int(pt[0]))), max(0, min(1000, int(pt[1])))]
                        except (ValueError, TypeError):
                            logger.warning(f"坐标包含无效字符，丢弃: {pt}")
                            del params["point"]

                if "text" in params:
                    del params["text"]

            elif action == ACTION_SCROLL:
                for key in ["start_point", "end_point"]:
                    if key in params:
                        p = params[key]
                        if isinstance(p, list) and len(p) >= 2:
                            if isinstance(p[0], list):
                                p = p[0]
                            try:
                                params[key] = [max(0, min(1000, int(p[0]))), max(0, min(1000, int(p[1])))]
                            except (ValueError, TypeError):
                                pass

            # 动作白名单过滤
            if action not in {ACTION_CLICK, ACTION_SCROLL, ACTION_TYPE, ACTION_OPEN, ACTION_COMPLETE}:
                action = ACTION_COMPLETE

            return AgentOutput(
                action=action,
                parameters=params,
                raw_output=raw_content,
                usage=self.extract_usage_info(response)
            )

        except Exception as e:
            logger.error(f"Agent 运行异常: {str(e)}", exc_info=True)
            return AgentOutput(action=ACTION_COMPLETE, parameters={}, raw_output=str(e), usage=UsageInfo())

    def _parse_json_robustly(self, text: str) -> Dict[str, Any]:
        """极限容错 JSON 解析：专治各种非法标点和多余文本"""
        cleaned = re.sub(r'//.*', '', text)
        cleaned = re.sub(r',\s*}', '}', cleaned)
        cleaned = re.sub(r',\s*]', ']', cleaned)

        try:
            return json.loads(cleaned)
        except:
            match = re.search(r'```json\s*(.*?)\s*```', cleaned, re.DOTALL | re.IGNORECASE)
            if match:
                try:
                    return json.loads(match.group(1))
                except:
                    pass

            start = cleaned.find('{')
            end = cleaned.rfind('}')
            if start != -1 and end != -1:
                try:
                    return json.loads(cleaned[start:end+1])
                except:
                    pass

        fallback = {"action": "COMPLETE", "parameters": {}}
        act_m = re.search(r'"action"\s*:\s*"([A-Z_]+)"', text, re.IGNORECASE)
        if act_m:
            fallback["action"] = act_m.group(1).upper()

        pt_m = re.search(r'"point"\s*:\s*\[\s*(\d+)\s*,\s*(\d+)\s*\]', cleaned)
        if pt_m:
            fallback["parameters"]["point"] = [int(pt_m.group(1)), int(pt_m.group(2))]

        text_m = re.search(r'"text"\s*:\s*"([^"]+)"', cleaned)
        if text_m:
            fallback["parameters"]["text"] = text_m.group(1)

        app_m = re.search(r'"app_name"\s*:\s*"([^"]+)"', cleaned)
        if app_m:
            fallback["parameters"]["app_name"] = app_m.group(1)

        return fallback
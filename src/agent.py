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

# 加载环境变量
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

logger = logging.getLogger(__name__)


class Agent(BaseAgent):
<<<<<<< HEAD
    """
    终极护航版 Agent：修复了坐标变量输出、键名错误以及特定的视觉动作误判
    """

    def reset(self):
        """重置内部状态"""
=======
    """Web 自动化 Agent，基于原始基线优化"""

    def reset(self):
        """每个测试用例开始前重置内部状态"""
>>>>>>> e37a634b419f2542f0ccd217a238e057b295eb75
        self.internal_history = []
        logger.info("--- 任务重置：开始新的测试用例 ---")

    def _build_system_prompt(self, instruction: str) -> str:
<<<<<<< HEAD
        return f"""你是一个顶尖的安卓手机 GUI 自动化代理。
=======
        """生成系统提示词"""
        return f"""你是一个智能手机 GUI 自动化助手。
>>>>>>> e37a634b419f2542f0ccd217a238e057b295eb75
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
        """决策主函数"""
        try:
<<<<<<< HEAD
            history_text = ""
            if input_data.history_actions:
                last_act = input_data.history_actions[-1]
                history_text = f"【提示】你上一步执行了: {last_act['action']}，参数为: {last_act['parameters']}。\n"
                if last_act['action'] == ACTION_TYPE:
                    history_text += "【注意】上一步已输入文字，请检查是否需要点击发送/搜索按钮，或者点击下拉联想词。尽量避免连续两次 TYPE。\n"
                elif last_act['action'] == ACTION_CLICK:
                    history_text += "【注意】如果上一步你点击的是输入框并且键盘已弹出，这一步请直接使用 TYPE 打字。如果不是，请根据需要继续操作。\n"
=======
            # 上一步操作记录，避免重复动作
            history_text = ""
            if input_data.history_actions:
               # 读取最近 3 步
               recent_history = input_data.history_actions[-3:]

               history_lines = []
    
               for idx, act in enumerate(recent_history):
                 step_desc = (
                     f"第{-len(recent_history)+idx}步: "
                     f"动作={act['action']}, "
                     f"参数={act['parameters']}"
                 )
                 history_lines.append(step_desc)

               history_text = "【最近操作历史】\n" + "\n".join(history_lines) + "\n"
>>>>>>> e37a634b419f2542f0ccd217a238e057b295eb75

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

<<<<<<< HEAD
=======
            # 调用大模型 API
>>>>>>> e37a634b419f2542f0ccd217a238e057b295eb75
            response = self._call_api(messages, temperature=0.1)
            raw_content = response.choices[0].message.content
            logger.info(f"模型原始输出: {raw_content}")

<<<<<<< HEAD
            parsed_data = self._parse_json_robustly(raw_content)
=======
            # 从返回内容中提取 JSON
            parsed_data = self._parse_json_from_text(raw_content)

>>>>>>> e37a634b419f2542f0ccd217a238e057b295eb75
            action = parsed_data.get("action", ACTION_COMPLETE).upper()
            params = parsed_data.get("parameters", {})
            if not isinstance(params, dict):
                params = {}

<<<<<<< HEAD
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
=======
            # 限制动作类型在白名单内
            legal_actions = {ACTION_CLICK, ACTION_SCROLL, ACTION_TYPE, ACTION_OPEN, ACTION_COMPLETE}
            if action not in legal_actions:
                action = ACTION_COMPLETE

            # --- 参数格式兜底处理 ---

            # 修复 OPEN 动作的应用名提取
            if action == ACTION_OPEN:
                # 兼容 app_name / app / name 三种 key
                app_name = params.get("app_name", params.get("app", params.get("name", "")))
                params = {"app_name": app_name}

            # 修复 CLICK 坐标：值域裁剪、展平嵌套列表
            elif action == ACTION_CLICK and "point" in params:
                try:
                    pt = params["point"]
                    if isinstance(pt, list) and len(pt) > 0 and isinstance(pt[0], list):
                        pt = pt[0]
                    params["point"] = [
                        max(0, min(1000, int(pt[0]))),
                        max(0, min(1000, int(pt[1])))
                    ]
                except Exception as e:
                    logger.warning(f"CLICK坐标解析异常，保留原样: {e}")

            # 修复 SCROLL 坐标：值域裁剪、展平嵌套列表
            elif action == ACTION_SCROLL:
                try:
                    if "start_point" in params:
                        sp = params["start_point"]
                        if isinstance(sp, list) and len(sp) > 0 and isinstance(sp[0], list):
                            sp = sp[0]
                        params["start_point"] = [
                            max(0, min(1000, int(sp[0]))),
                            max(0, min(1000, int(sp[1])))
                        ]
                    if "end_point" in params:
                        ep = params["end_point"]
                        if isinstance(ep, list) and len(ep) > 0 and isinstance(ep[0], list):
                            ep = ep[0]
                        params["end_point"] = [
                            max(0, min(1000, int(ep[0]))),
                            max(0, min(1000, int(ep[1])))
                        ]
                except Exception as e:
                    logger.warning(f"SCROLL坐标解析异常，保留原样: {e}")
>>>>>>> e37a634b419f2542f0ccd217a238e057b295eb75

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

<<<<<<< HEAD
        try:
            return json.loads(cleaned)
        except:
            match = re.search(r'```json\s*(.*?)\s*```', cleaned, re.DOTALL | re.IGNORECASE)
=======
    def _parse_json_from_text(self, text: str) -> Dict[str, Any]:
        """从文本中提取 JSON，增强容错性"""
        try:
            return json.loads(text)
        except Exception:
            # 尝试匹配 ```json ... ``` 代码块
            match = re.search(r'json\s*(.*?)\s*', text, re.DOTALL | re.IGNORECASE)
>>>>>>> e37a634b419f2542f0ccd217a238e057b295eb75
            if match:
                try:
                    return json.loads(match.group(1))
                except Exception:
                    pass

<<<<<<< HEAD
            start = cleaned.find('{')
            end = cleaned.rfind('}')
            if start != -1 and end != -1:
                try:
                    return json.loads(cleaned[start:end+1])
                except:
=======
            # 提取第一个 { 到最后一个 } 之间的内容
            start = text.find('{')
            end = text.rfind('}')
            if start != -1 and end != -1:
                try:
                    return json.loads(text[start:end+1])
                except Exception:
>>>>>>> e37a634b419f2542f0ccd217a238e057b295eb75
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
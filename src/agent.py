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
    基于 36.36% 高分基线的稳定优化版 Agent
    """

    def reset(self):
        """每个测试用例开始前调用"""
        self.internal_history = []
        logger.info("--- 新任务开始，重置状态 ---")

    def _build_system_prompt(self, instruction: str) -> str:
        """构建强制 JSON 输出的系统提示词"""
        return f"""你是一个智能手机 GUI 自动化助手。
【任务目标】：{instruction}

【操作准则 - 必读】：
1. 你必须仔细对比【当前屏幕截图】和【任务目标】。
2. ⚠️ 完结判定：如果你观察到任务已经完成（例如：评论已经显示发布成功、页面已经跳转到最终目的地），你必须输出 ACTION 为 "COMPLETE"！
3. 防重复输入：如果你的上一步是输入文本（TYPE），下一步通常需要寻找并点击“发送”、“发布”或“搜索”等按钮，尽量避免连续两次输入。
4. 坐标必须在 [0, 1000] 范围内。左上角为 [0, 0]，右下角为 [1000, 1000]。

【输出格式要求】：
请严格以 JSON 格式输出，必须包含 thought、action 和 parameters 三个字段：
```json
{{
    "thought": "简要描述当前界面状态，回忆上一步，判断是否已完成",
    "action": "CLICK 或 TYPE 或 SCROLL 或 OPEN 或 COMPLETE",
    "parameters": {{相关参数}}
}}
【动作参数示例】：

任务完成: {{"action": "COMPLETE", "parameters": {{}}}}

点击: {{"action": "CLICK", "parameters": {{"point": [500, 500]}}}}

输入: {{"action": "TYPE", "parameters": {{"text": "要输入的内容"}}}}

滑动: {{"action": "SCROLL", "parameters": {{"start_point": [500, 800], "end_point": [500, 200]}}}}

打开应用: {{"action": "OPEN", "parameters": {{"app_name": "应用名"}}}}
"""

    def act(self, input_data: AgentInput) -> AgentOutput:
        """核心决策逻辑"""
        try:
            # 记录历史操作信息，防止 AI 原地打转
            history_text = ""
            if input_data.history_actions:
                last_act = input_data.history_actions[-1]
                history_text = f"【注意】你上一步执行了动作: {last_act['action']}，参数: {last_act['parameters']}。\n"

            messages = [
                {"role": "system", "content": self._build_system_prompt(input_data.instruction)},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": f"当前是第 {input_data.step_count} 步。\n{history_text}请观察最新截图，判断任务是否已经完成？如果已完成请输出 COMPLETE，否则给出下一步。"},
                        {"type": "image_url", "image_url": {"url": self._encode_image(input_data.current_image)}}
                    ]
                }
            ]

            # 调用 API
            response = self._call_api(messages, temperature=0.1)
            raw_content = response.choices[0].message.content
            logger.info(f"模型原始输出: {raw_content}")

            # 解析 JSON 结果
            parsed_data = self._parse_json_from_text(raw_content)

            action = parsed_data.get("action", ACTION_COMPLETE).upper()
            params = parsed_data.get("parameters", {})

            # 确保动作在合法范围内
            legal_actions = {ACTION_CLICK, ACTION_SCROLL, ACTION_TYPE, ACTION_OPEN, ACTION_COMPLETE}
            if action not in legal_actions:
                action = ACTION_COMPLETE

            # === 最安全的参数修复区（解决日志里的具体报错，不抛异常） ===

            # 1. 修复 OPEN 参数不匹配 (解决 expect '爱奇艺', got '' 的问题)
            if action == ACTION_OPEN:
                # 无论模型输出 app, name 还是 app_name，统统安全提取
                app_name = params.get("app_name", params.get("app", params.get("name", "")))
                params = {"app_name": app_name}

            # 2. 修复 CLICK 坐标格式 (防止超出 1000 或出现嵌套列表)
            elif action == ACTION_CLICK and "point" in params:
                try:
                    pt = params["point"]
                    if isinstance(pt, list) and len(pt) > 0 and isinstance(pt[0], list):
                        pt = pt[0]  # 兼容 [[x, y]] 的错误格式
                    params["point"] = [max(0, min(1000, int(pt[0]))), max(0, min(1000, int(pt[1])))]
                except Exception as e:
                    logger.warning(f"CLICK坐标解析异常，保留原样: {e}")

            # 3. 修复 SCROLL 坐标格式
            elif action == ACTION_SCROLL:
                try:
                    if "start_point" in params:
                        sp = params["start_point"]
                        if isinstance(sp, list) and len(sp) > 0 and isinstance(sp[0], list):
                            sp = sp[0]
                        params["start_point"] = [max(0, min(1000, int(sp[0]))), max(0, min(1000, int(sp[1])))]
                    if "end_point" in params:
                        ep = params["end_point"]
                        if isinstance(ep, list) and len(ep) > 0 and isinstance(ep[0], list):
                            ep = ep[0]
                        params["end_point"] = [max(0, min(1000, int(ep[0]))), max(0, min(1000, int(ep[1])))]
                except Exception as e:
                    logger.warning(f"SCROLL坐标解析异常，保留原样: {e}")

            return AgentOutput(
                action=action,
                parameters=params,
                raw_output=raw_content,
                usage=self.extract_usage_info(response)
            )

        except Exception as e:
            logger.error(f"执行出错: {str(e)}", exc_info=True)
            return AgentOutput(
                action=ACTION_COMPLETE,
                parameters={},
                raw_output=f"Error: {str(e)}",
                usage=UsageInfo()
            )

    def _parse_json_from_text(self, text: str) -> Dict[str, Any]:
        """从文本中提取 JSON，增强鲁棒性"""
        try:
            return json.loads(text)
        except:
            # 正则提取 json ...  块
            match = re.search(r'json\s*(.*?)\s*', text, re.DOTALL | re.IGNORECASE)
            if match:
                try:
                    return json.loads(match.group(1))
                except:
                    pass

            # 寻找第一个 { 和最后一个 }
            start = text.find('{')
            end = text.rfind('}')
            if start != -1 and end != -1:
                try:
                    return json.loads(text[start:end+1])
                except:
                    pass

        return {"action": ACTION_COMPLETE, "parameters": {}}
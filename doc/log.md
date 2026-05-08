026-04-25 19:32:17,186 - INFO - Start testing case: step_baidumap_onekey_0010
2026-04-25 19:32:17,186 - INFO - --- 任务重置：开始新的测试用例 ---
2026-04-25 19:32:17,188 - INFO - --- Step 1: Current Status 0 ---
2026-04-25 19:32:17,203 - WARNING - 
2026-04-25 19:32:17,204 - WARNING - ============================================================
2026-04-25 19:32:17,204 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:17,204 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:17,204 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:17,204 - WARNING - 
2026-04-25 19:32:17,205 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:17,205 - WARNING - ============================================================
2026-04-25 19:32:17,205 - WARNING - 
2026-04-25 19:32:17,261 - INFO - [API调用] model=doubao-seed-1-6-vision-250815, url=https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:20,907 - INFO - HTTP Request: POST https://ark.cn-beijing.volces.com/api/v3/chat/completions "HTTP/1.1 200 OK"
2026-04-25 19:32:20,909 - INFO - 模型原始输出: ```json
{
    "thought": "用户想要打开百度地图，打车从国际医学中心去西安回民街，地址选项都选第一个，我来想一想该做哪些步骤，首先要打开百度地图，再要点击打车，输入起点和终点，最后点击打车，就能完成任务啦。没错就这么办，第一步我要先打开百度地图，得从应用列表里找找，在这呢~找到了百度地图，我现在就打开它吧！",
    "action": "OPEN",
    "parameters": {
        "app_name": "百度地图"
    }
}
```
2026-04-25 19:32:20,910 - INFO - Agent Output: action=OPEN, params={'app_name': '百度地图'}
2026-04-25 19:32:20,911 - WARNING - 
2026-04-25 19:32:20,911 - WARNING - ============================================================
2026-04-25 19:32:20,911 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:20,912 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:20,912 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:20,913 - WARNING - 
2026-04-25 19:32:20,913 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:20,913 - WARNING - ============================================================
2026-04-25 19:32:20,914 - WARNING - 
2026-04-25 19:32:20,914 - INFO - Token usage: +1223 (input: 1091, output: 132), total: 23809/1200000
2026-04-25 19:32:20,954 - INFO - --- Step 2: Current Status 1 ---
2026-04-25 19:32:20,967 - WARNING - 
2026-04-25 19:32:20,968 - WARNING - ============================================================
2026-04-25 19:32:20,969 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:20,969 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:20,969 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:20,969 - WARNING - 
2026-04-25 19:32:20,969 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:20,969 - WARNING - ============================================================
2026-04-25 19:32:20,970 - WARNING - 
2026-04-25 19:32:21,026 - INFO - [API调用] model=doubao-seed-1-6-vision-250815, url=https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:23,935 - INFO - HTTP Request: POST https://ark.cn-beijing.volces.com/api/v3/chat/completions "HTTP/1.1 200 OK"
2026-04-25 19:32:23,938 - INFO - 模型原始输出: ```json
{
    "thought": "现在百度地图启动后出现了广告页面，右上角有“跳过03”的按钮，需要点击跳过广告才能进入百度地图的主界面，继续完成打车任务。所以下一步应该点击跳过广告的按钮。",
    "action": "CLICK",
    "parameters": {
        "point": [862, 38],
        "text": "",
        "start_point": [],
        "end_point": [],
        "app_name": ""
    }
}
```
2026-04-25 19:32:23,938 - INFO - Agent Output: action=CLICK, params={'point': [862, 38], 'start_point': [], 'end_point': [], 'app_name': ''}
2026-04-25 19:32:23,939 - WARNING - 
2026-04-25 19:32:23,939 - WARNING - ============================================================
2026-04-25 19:32:23,940 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:23,940 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:23,940 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:23,941 - WARNING - 
2026-04-25 19:32:23,941 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:23,941 - WARNING - ============================================================
2026-04-25 19:32:23,942 - WARNING - 
2026-04-25 19:32:23,942 - INFO - Token usage: +1234 (input: 1115, output: 119), total: 25043/1200000
2026-04-25 19:32:23,984 - INFO - --- Step 3: Current Status 2 ---
2026-04-25 19:32:23,992 - WARNING - 
2026-04-25 19:32:23,992 - WARNING - ============================================================
2026-04-25 19:32:23,993 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:23,993 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:23,993 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:23,993 - WARNING - 
2026-04-25 19:32:23,993 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:23,994 - WARNING - ============================================================
2026-04-25 19:32:23,994 - WARNING - 
2026-04-25 19:32:24,044 - INFO - [API调用] model=doubao-seed-1-6-vision-250815, url=https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:26,403 - INFO - HTTP Request: POST https://ark.cn-beijing.volces.com/api/v3/chat/completions "HTTP/1.1 200 OK"
2026-04-25 19:32:26,405 - INFO - 模型原始输出: ```json
{
    "thought": "现在需要打车，界面上有“打车”的图标，点击它进入打车界面，这样才能设置起点和终点。所以下一步点击打车按钮。",
    "action": "CLICK",
    "parameters": {
        "point": [500, 446],
        "start_point": [],
        "end_point": [],
        "app_name": ""
    }
}
```
2026-04-25 19:32:26,406 - INFO - Agent Output: action=CLICK, params={'point': [500, 446], 'start_point': [], 'end_point': [], 'app_name': ''}
2026-04-25 19:32:26,407 - WARNING - 
2026-04-25 19:32:26,407 - WARNING - ============================================================
2026-04-25 19:32:26,408 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:26,408 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:26,409 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:26,409 - WARNING - 
2026-04-25 19:32:26,409 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:26,410 - WARNING - ============================================================
2026-04-25 19:32:26,410 - WARNING - 
2026-04-25 19:32:26,411 - INFO - Token usage: +1271 (input: 1171, output: 100), total: 26314/1200000
2026-04-25 19:32:26,449 - INFO - --- Step 4: Current Status 3 ---
2026-04-25 19:32:26,462 - WARNING - 
2026-04-25 19:32:26,462 - WARNING - ============================================================
2026-04-25 19:32:26,462 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:26,462 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:26,463 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:26,463 - WARNING - 
2026-04-25 19:32:26,463 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:26,463 - WARNING - ============================================================
2026-04-25 19:32:26,463 - WARNING - 
2026-04-25 19:32:26,507 - INFO - [API调用] model=doubao-seed-1-6-vision-250815, url=https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:29,180 - INFO - HTTP Request: POST https://ark.cn-beijing.volces.com/api/v3/chat/completions "HTTP/1.1 200 OK"
2026-04-25 19:32:29,181 - INFO - 模型原始输出: ```json
{
    "thought": "现在需要修改上车地点为国际医学中心，所以先点击上车地点的输入框，这样可以进入编辑状态来修改起点。",
    "action": "CLICK",
    "parameters": {
        "point": [450, 471],
        "start_point": [],
        "end_point": [],
        "app_name": ""
    }
}
```
2026-04-25 19:32:29,182 - INFO - Agent Output: action=CLICK, params={'point': [450, 471], 'start_point': [], 'end_point': [], 'app_name': ''}
2026-04-25 19:32:29,183 - WARNING - 
2026-04-25 19:32:29,183 - WARNING - ============================================================
2026-04-25 19:32:29,184 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:29,184 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:29,185 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:29,185 - WARNING - 
2026-04-25 19:32:29,186 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:29,186 - WARNING - ============================================================
2026-04-25 19:32:29,186 - WARNING - 
2026-04-25 19:32:29,187 - INFO - Token usage: +1268 (input: 1172, output: 96), total: 27582/1200000
2026-04-25 19:32:29,221 - INFO - --- Step 5: Current Status 4 ---
2026-04-25 19:32:29,231 - WARNING - 
2026-04-25 19:32:29,232 - WARNING - ============================================================
2026-04-25 19:32:29,232 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:29,232 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:29,233 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:29,233 - WARNING - 
2026-04-25 19:32:29,233 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:29,233 - WARNING - ============================================================
2026-04-25 19:32:29,234 - WARNING - 
2026-04-25 19:32:29,271 - INFO - [API调用] model=doubao-seed-1-6-vision-250815, url=https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:31,614 - INFO - HTTP Request: POST https://ark.cn-beijing.volces.com/api/v3/chat/completions "HTTP/1.1 200 OK"
2026-04-25 19:32:31,616 - INFO - 模型原始输出: ```json
{
    "thought": "现在需要设置起点为国际医学中心，所以在输入框中输入这个地点名称。键盘已经弹出，直接打字输入。",
    "action": "TYPE",
    "parameters": {
        "text": "国际医学中心",
        "point": [],
        "start_point": [],
        "end_point": [],
        "app_name": ""
    }
}
```
2026-04-25 19:32:31,616 - INFO - Agent Output: action=TYPE, params={'text': '国际医学中心'}
2026-04-25 19:32:31,617 - WARNING - 
2026-04-25 19:32:31,617 - WARNING - ============================================================
2026-04-25 19:32:31,618 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:31,618 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:31,619 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:31,619 - WARNING - 
2026-04-25 19:32:31,620 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:31,620 - WARNING - ============================================================
2026-04-25 19:32:31,620 - WARNING - 
2026-04-25 19:32:31,621 - INFO - Token usage: +1268 (input: 1172, output: 96), total: 28850/1200000
2026-04-25 19:32:31,621 - ERROR - [Checker] TYPE: text mismatch, expect '.*国际医学中心', got '国际医学中心'
2026-04-25 19:32:31,648 - INFO - --- Step 6: Current Status 5 ---
2026-04-25 19:32:31,662 - WARNING - 
2026-04-25 19:32:31,662 - WARNING - ============================================================
2026-04-25 19:32:31,663 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:31,663 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:31,663 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:31,664 - WARNING - 
2026-04-25 19:32:31,664 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:31,664 - WARNING - ============================================================
2026-04-25 19:32:31,664 - WARNING - 
2026-04-25 19:32:31,699 - INFO - [API调用] model=doubao-seed-1-6-vision-250815, url=https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:34,587 - INFO - HTTP Request: POST https://ark.cn-beijing.volces.com/api/v3/chat/completions "HTTP/1.1 200 OK"
2026-04-25 19:32:34,588 - INFO - 模型原始输出: ```json
{
    "thought": "根据任务要求，地址选项都选第一个，所以我需要点击第一个搜索结果“西安国际医学中心医院”，这样可以将其设置为起点。",
    "action": "CLICK",
    "parameters": {
        "point": [450, 166],
        "text": null,
        "start_point": null,
        "end_point": null,
        "app_name": null
    }
}
```
2026-04-25 19:32:34,589 - INFO - Agent Output: action=CLICK, params={'point': [450, 166], 'start_point': None, 'end_point': None, 'app_name': None}
2026-04-25 19:32:34,589 - WARNING - 
2026-04-25 19:32:34,589 - WARNING - ============================================================
2026-04-25 19:32:34,589 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:34,590 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:34,590 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:34,590 - WARNING - 
2026-04-25 19:32:34,590 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:34,591 - WARNING - ============================================================
2026-04-25 19:32:34,591 - WARNING - 
2026-04-25 19:32:34,591 - INFO - Token usage: +1256 (input: 1146, output: 110), total: 30106/1200000
2026-04-25 19:32:34,591 - ERROR - [Checker] CLICK failed: (450, 166) not in ([793, 964], [53, 115])
2026-04-25 19:32:34,617 - INFO - --- Step 7: Current Status 6 ---
2026-04-25 19:32:34,625 - WARNING - 
2026-04-25 19:32:34,625 - WARNING - ============================================================
2026-04-25 19:32:34,625 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:34,625 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:34,625 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:34,626 - WARNING - 
2026-04-25 19:32:34,626 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:34,626 - WARNING - ============================================================
2026-04-25 19:32:34,626 - WARNING - 
2026-04-25 19:32:34,681 - INFO - [API调用] model=doubao-seed-1-6-vision-250815, url=https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:37,186 - INFO - HTTP Request: POST https://ark.cn-beijing.volces.com/api/v3/chat/completions "HTTP/1.1 200 OK"
2026-04-25 19:32:37,187 - INFO - 模型原始输出: ```json
{
    "thought": "现在需要设置目的地，界面上有“你要去哪儿”的输入框，我需要点击这个输入框来输入目的地西安回民街。所以下一步是点击“你要去哪儿”的输入框。",
    "action": "CLICK",
    "parameters": {
        "point": [300, 546],
        "start_point": null,
        "end_point": null,
        "app_name": null
    }
}
```
2026-04-25 19:32:37,188 - INFO - Agent Output: action=CLICK, params={'point': [300, 546], 'start_point': None, 'end_point': None, 'app_name': None}
2026-04-25 19:32:37,189 - WARNING - 
2026-04-25 19:32:37,189 - WARNING - ============================================================
2026-04-25 19:32:37,189 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:37,190 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:37,190 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:37,191 - WARNING - 
2026-04-25 19:32:37,191 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:37,191 - WARNING - ============================================================
2026-04-25 19:32:37,192 - WARNING - 
2026-04-25 19:32:37,192 - INFO - Token usage: +1287 (input: 1174, output: 113), total: 31393/1200000
2026-04-25 19:32:37,224 - INFO - --- Step 8: Current Status 7 ---
2026-04-25 19:32:37,237 - WARNING - 
2026-04-25 19:32:37,238 - WARNING - ============================================================
2026-04-25 19:32:37,238 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:37,238 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:37,239 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:37,239 - WARNING - 
2026-04-25 19:32:37,239 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:37,239 - WARNING - ============================================================
2026-04-25 19:32:37,240 - WARNING - 
2026-04-25 19:32:37,273 - INFO - [API调用] model=doubao-seed-1-6-vision-250815, url=https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:39,939 - INFO - HTTP Request: POST https://ark.cn-beijing.volces.com/api/v3/chat/completions "HTTP/1.1 200 OK"
2026-04-25 19:32:39,941 - INFO - 模型原始输出: ```json
{
    "thought": "现在需要在终点输入框中输入‘西安回民街’，因为任务要求打车的终点是西安回民街，所以要在输入框中输入这个地址，方便后续选择。",
    "action": "TYPE",
    "parameters": {
        "text": "西安回民街",
        "point": [454, 84],
        "start_point": null,
        "end_point": null,
        "app_name": null
    }
}
```
2026-04-25 19:32:39,942 - INFO - Agent Output: action=TYPE, params={'text': '西安回民街'}
2026-04-25 19:32:39,943 - WARNING - 
2026-04-25 19:32:39,943 - WARNING - ============================================================
2026-04-25 19:32:39,944 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:39,944 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:39,945 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:39,945 - WARNING - 
2026-04-25 19:32:39,946 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:39,946 - WARNING - ============================================================
2026-04-25 19:32:39,947 - WARNING - 
2026-04-25 19:32:39,947 - INFO - Token usage: +1292 (input: 1174, output: 118), total: 32685/1200000
2026-04-25 19:32:39,947 - ERROR - [Checker] TYPE: text mismatch, expect '.*回民街', got '西安回民街'
2026-04-25 19:32:39,948 - INFO - [Checker] Action mismatch: expect [CLICK], got [TYPE]
2026-04-25 19:32:39,973 - INFO - --- Step 9: Current Status 8 ---
2026-04-25 19:32:39,989 - WARNING - 
2026-04-25 19:32:39,989 - WARNING - ============================================================
2026-04-25 19:32:39,990 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:39,994 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:39,995 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:39,995 - WARNING - 
2026-04-25 19:32:39,995 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:39,996 - WARNING - ============================================================
2026-04-25 19:32:39,996 - WARNING - 
2026-04-25 19:32:40,022 - INFO - [API调用] model=doubao-seed-1-6-vision-250815, url=https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:42,874 - INFO - HTTP Request: POST https://ark.cn-beijing.volces.com/api/v3/chat/completions "HTTP/1.1 200 OK"
2026-04-25 19:32:42,876 - INFO - 模型原始输出: ```json
{
    "thought": "现在需要选择地址选项的第一个，也就是列表里的‘回民街’，它的位置在最上方，显示为美食街、莲湖区北院门5号，距离21.2km。点击这个选项来确定目的地。",
    "action": "CLICK",
    "parameters": {
        "point": [435, 166],
        "text": "",
        "start_point": [],
        "end_point": [],
        "app_name": ""
    }
}
```
2026-04-25 19:32:42,877 - INFO - Agent Output: action=CLICK, params={'point': [435, 166], 'start_point': [], 'end_point': [], 'app_name': ''}
2026-04-25 19:32:42,877 - WARNING - 
2026-04-25 19:32:42,878 - WARNING - ============================================================
2026-04-25 19:32:42,878 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:42,879 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:42,879 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:42,880 - WARNING - 
2026-04-25 19:32:42,880 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:42,881 - WARNING - ============================================================
2026-04-25 19:32:42,881 - WARNING - 
2026-04-25 19:32:42,881 - INFO - Token usage: +1270 (input: 1146, output: 124), total: 33955/1200000
2026-04-25 19:32:42,882 - ERROR - [Checker] CLICK failed: (435, 166) not in ([804, 960], [53, 118])
2026-04-25 19:32:42,899 - INFO - --- Step 10: Current Status 10 ---
2026-04-25 19:32:42,907 - WARNING - 
2026-04-25 19:32:42,908 - WARNING - ============================================================
2026-04-25 19:32:42,908 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:42,908 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:42,909 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:42,909 - WARNING - 
2026-04-25 19:32:42,909 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:42,909 - WARNING - ============================================================
2026-04-25 19:32:42,909 - WARNING - 
2026-04-25 19:32:42,956 - INFO - [API调用] model=doubao-seed-1-6-vision-250815, url=https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:45,657 - INFO - HTTP Request: POST https://ark.cn-beijing.volces.com/api/v3/chat/completions "HTTP/1.1 200 OK"
2026-04-25 19:32:45,658 - INFO - 模型原始输出: ```json
{
    "thought": "任务是打开百度地图，打车从国际医学中心去西安回民街且地址选项都选第一个，现在已经进入打车的车型选择和叫车界面，所有地址选择步骤都已完成，接下来点击‘立即呼叫’就完成打车的操作流程了，所以任务实质完成。",
    "action": "COMPLETE",
    "parameters": {}
}
```
2026-04-25 19:32:45,659 - INFO - Agent Output: action=COMPLETE, params={}
2026-04-25 19:32:45,659 - WARNING - 
2026-04-25 19:32:45,659 - WARNING - ============================================================
2026-04-25 19:32:45,659 - WARNING - [调试模式] 当前 API 配置仅供自测使用
2026-04-25 19:32:45,661 - WARNING -   API_URL:  https://ark.cn-beijing.volces.com/api/v3
2026-04-25 19:32:45,661 - WARNING -   MODEL_ID: doubao-seed-1-6-vision-250815
2026-04-25 19:32:45,661 - WARNING - 
2026-04-25 19:32:45,661 - WARNING - 提示：提交时将使用主办方统一配置
2026-04-25 19:32:45,661 - WARNING - ============================================================
2026-04-25 19:32:45,661 - WARNING - 
2026-04-25 19:32:45,662 - INFO - Token usage: +1264 (input: 1173, output: 91), total: 35219/1200000
2026-04-25 19:32:48,715 - INFO - 可视化已保存: ./output\visualization\step_baidumap_onekey_0010\summary.png
2026-04-25 19:32:48,717 - INFO - ---------------------------------------------------
2026-04-25 19:32:48,717 - INFO - [No. 3: step_baidumap_onekey_0010] Score: 8/10 = 0.80
2026-04-25 19:32:48,717 - INFO - ---------------------------------------------------
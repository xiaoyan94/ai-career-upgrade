## DAY3 通过限制上下文长度，只保留最近几轮对话，避免 token 无限增长，从而控制成本和响应速度。

如何控制 token？

如何避免上下文过长？

如何管理多轮对话？

会做上下文裁剪

理解 token 增长问题

会做人设控制

有基础成本意识

## DAY2 把一次性问答，升级成“可持续对话”的命令行聊天工具。

✅ API 调用

✅ 多轮对话

✅ 上下文记忆

✅ Token 观察

会管理对话历史

理解 system 的作用

理解上下文依赖

知道 token 会累积

知道成本和长度有关

## 报错表示没钱了 需要充值

```bash
File "/Users/yanweiming/ai-career-upgrade/venv/lib/python3.14/site-packages/openai/_base_client.py", line 1070, in request
    raise self._make_status_error_from_response(err.response) from None
openai.APIStatusError: Error code: 402 - {'error': {'message': 'Insufficient Balance', 'type': 'unknown_error', 'param': None, 'code': 'invalid_request_error'}}
(venv)  ✘ 
```

## DAY1 调通API

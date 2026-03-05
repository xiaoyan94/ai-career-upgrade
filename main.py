import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://api.deepseek.com"
)

total_tokens = 0

role_input = input("请输入AI角色（例如：Java架构师）：")

messages = [
    {"role": "system", "content": "你是一个专业的{role_input}"}
]

def trim_messages(messages, max_history=6):
    """
    保留最近 max_history 条 user/assistant 对话
    """
    system_msg = messages[0]
    history = messages[1:]

    # 只保留最近几条
    history = history[-max_history:]

    return [system_msg] + history

while True:
    user_input = input("你: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("对话结束")
        break

    messages.append({"role": "user", "content": user_input})
    
    trimmed = trim_messages(messages)

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=trimmed
    )

    reply = response.choices[0].message.content
    
    print("AI:", reply)
    
    messages.append({"role": "assistant", "content": reply})

    print("Token使用:", response.usage)

    total_tokens += response.usage.total_tokens
    print("累计Token:", total_tokens)

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://api.deepseek.com"
)

messages = [
    {"role": "system", "content": "你是一个专业的汉语言文学专家"}
]

while True:
    user_input = input("你: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("对话结束")
        break

    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )

    reply = response.choices[0].message.content
    
    print("AI:", reply)
    
    messages.append({"role": "assistant", "content": reply})

    print("Token使用:", response.usage)

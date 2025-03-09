import json
from dotenv import load_dotenv
from dialog_memory import handle_new_message
from llm_online import get_response


load_dotenv()
messages = [
    # {"role": "system", "content": "You are Qwen, a helpful assistant."},
    {"role": "user", "content": "去年5月最后一天的日期是啥?"}
]

while True:

    message = get_response(messages)

    messages = handle_new_message(message, messages)

    if message["role"] == "assistant" and '</think>' in message["content"]:
        break

# 将messages 保存到本地文件
with open("messages.json", "w", encoding="utf-8") as f:
    json.dump(messages, f, ensure_ascii=False, indent=4)

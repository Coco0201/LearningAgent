import requests
import os
from tools_list import tools

url = "https://api.siliconflow.cn/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.getenv('siliconflow_api_key')}",
    "Content-Type": "application/json"
}

def get_response(messages):
    payload = {
        "model": "Qwen/QwQ-32B",
        "messages": messages,
        "stream": False,
        "max_tokens": 512,
        "stop": None,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "response_format": {"type": "text"},
        "tools": tools
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()["choices"][0]["message"]
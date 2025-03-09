import json

from functions import get_function_by_name


def handle_new_message(message, messages):
    if tool_calls := message.get("tool_calls", None):
        for tool_call in tool_calls:
            fn_name = tool_call["function"]["name"]
            fn_args = json.loads(tool_call["function"]["arguments"])

            # 假设有函数库 get_function_by_name
            fn_result = json.dumps(get_function_by_name(fn_name)(**fn_args))

            messages.append({
                "role": "tool",
                "content": fn_result,
                "tool_call_id": tool_call["id"]
            })
    else:
        messages.append({
            "role": message["role"],
            "content": message["content"]
        })
    return messages

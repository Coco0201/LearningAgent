tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_date",
            "description": "获取当前日期",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_year_calendar",
            "description": "获取某年的所有日历, 调用者需要以yyyy形式提供是哪一年",
            "parameters": {
                "type": "object",
                "properties": {
                    "year": {
                        "type": "string",
                        "description": "表达年的数字，例如2024,为yyyy的格式",
                    }
                },
                "required": ["year"]
            },
        }
    },
]
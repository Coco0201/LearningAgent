import calendar
from datetime import datetime


def get_function_by_name(func_name):
    funcs = {
        "get_current_date": get_current_date,
        "get_year_calendar": get_year_calendar
    }
    return funcs.get(func_name)


def get_year_calendar(year):
    # 创建一个TextCalendar实例
    cal = calendar.TextCalendar(calendar.SUNDAY)

    calenders = ''
    # 循环遍历一年中的每个月，并打印该月的日历
    for month in range(1, 13):  # 1月到12月
        calenders = calenders + f"{calendar.month_name[month]} {year}"
        calenders = f"{calenders}/n" + cal.formatmonth(int(year), month)
        calenders = f"{calenders}/n" + '-' * 20

    return calenders


def get_current_date():
    # 获取当前日期并格式化为字符串
    formatted_date = datetime.now().strftime('%Y-%m-%d')
    return f"当天日期为{formatted_date}"


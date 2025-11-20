from datetime import datetime

def format_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    formats = [
        "%Y/%m/%d", "%d-%b-%Y", "%d %B, %Y",
        "%Y年%m月%d日", "%d.%m.%Y", "%Y-%m-%d %H:%M:%S"
    ]
    formatted_dates = []
    for fmt in formats:
        formatted_dates.append(date_obj.strftime(fmt))
    return formatted_dates

# 测试
date_str = "2023-09-15"
formatted_dates = format_date(date_str)
for date in formatted_dates:
    print(date)
# 天天向上百分之一的力量:
# 假若对于学生， 一年365天，每天进步百分之一，一年后累计进步多少呢?
# 一年365天，每天退步百分之一，一年后累计退步多少呢?

def calculate_growth(start_value, daily_change, days):
    value = start_value
    for i in range(days):
        value *= (1 + daily_change)
    return value

# 初始值为1，表示100%
initial_value = 1.0

# 每天进步百分之一
daily_increase = 0.01
# 每天退步百分之一
daily_decrease = -0.01
# 天数为365天
days = 365

# 计算一年后每天进步百分之一的累计效果
final_value_increase = calculate_growth(initial_value, daily_increase, days)
print(f"一年后每天进步百分之一，累计进步: {final_value_increase * 100 - 100:.2f}%")

# 计算一年后每天退步百分之一的累计效果
final_value_decrease = calculate_growth(initial_value, daily_decrease, days)
print(f"一年后每天退步百分之一，累计退步: {100 - final_value_decrease * 100:.2f}%")

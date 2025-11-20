days = 365 # 365天
initial_value = 1.0 # 初始能力值
current_value = initial_value # 当前能力值
consecutive_days = 0  # 当前连续学习的天数
for day in range(1, days + 1):
    if consecutive_days < 3:# 前3天没有变化
        consecutive_days += 1# 连续天数加1
    elif consecutive_days < 7:# 第3天到第7天，每天增长为前一天的1%
        current_value *= 1.01# 第4天到第7天，每天增长为前一天的1%
        consecutive_days += 1# 连续天数加1
    else:
        consecutive_days = 0 # 完成一个7天周期，重置连续天数
    if day % 7 == 0 and day != days:# 模拟间断学习的情况
        consecutive_days = 0# 每7天的最后一天间断学习，重置连续天数
print("连续学习365天后的最终能力值: {:.2f}".format(current_value))# 输出结果
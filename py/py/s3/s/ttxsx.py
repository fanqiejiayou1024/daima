import math
def simulate_learning_with_rest(days, rest_interval):
    initial_value = 1.0# 初始能力值
    current_value = initial_value# 当前能力值
    consecutive_days = 0  # 当前连续学习的天数
    for day in range(1, days + 1):# 遍历每一天
        if day % rest_interval == 0:# 如果当前是休息日
            consecutive_days = 0# 每rest_interval天休息一天，重置连续天数
        else:
            if consecutive_days < 3:# 前3天没有变化
                consecutive_days += 1# 连续天数加1
            elif consecutive_days < 7:
                current_value *= 1.01# 第4天到第7天，每天增长为前一天的1%
                consecutive_days += 1# 更新连续天数
            else:
                consecutive_days = 0# 完成一个7天周期，重置连续天数
                return current_value# 返回当前能力值
if __name__ == "__main__":
    final_value_10 = simulate_learning_with_rest(365, 10)# 计算每10天休息一天，365天后的最终能力值
    print("每10天休息一天，365天后的最终能力值: {:.2f}".format(final_value_10))# 输出计算每10天休息一天，365天后的最终能力值
    final_value_15 = simulate_learning_with_rest(365, 15)# 计算每15天休息一天，365天后的最终能力值
    print("每15天休息一天，365天后的最终能力值: {:.2f}".format(final_value_15))# 输出计算每15天休息一天，365天后的最终能力值
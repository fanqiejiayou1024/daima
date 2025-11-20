import random

number_to_guess = random.randint(0, 9)#生成0-9之间的随机数
attempts = 0#尝试次数

while True:
    try:
        user_guess = int(input("请输入你猜测的数字（0-9）："))#输入一个数字用于比大小
        attempts += 1#尝试次数加一

        if user_guess < number_to_guess:#如果输入的数字小于比大小的数字
            print("太小了!")
        elif user_guess > number_to_guess:#如果输入的数字大于比大小的数字
            print("太大了!")
        else:
            print(f"恭喜你，猜对了!你总共猜了{attempts}次。")
            break
    except ValueError:#输入的不是数字
        print("请输入一个有效的数字!")

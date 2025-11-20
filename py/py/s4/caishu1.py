def guess_number(number):
    attempts = 0#尝试次数
    while True:#无限循环
        user_guess = int(input("请输入一个0-100之间的整数: "))#输入一个0-100数字用于比大小
        attempts += 1#尝试次数加一
        if user_guess > number: #如果输入的数字大于比大小的数字
            print("遗憾，太大了")#提示
        elif user_guess < number:#如果输入的数字小于比大小的数字
            print("遗憾，太小了")#提示
        else:
            print(f"预测{attempts}次，你猜中了!")#猜中输出
            break#跳出循环
if __name__ == "__main__":
    guess_number(50)#调用猜数字参数50
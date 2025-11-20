def hws(number):#判断是否为回文数的函数
    return str(number) == str(number)[::-1]#判断是否为回文数 str(number)将数字转换为字符串 [::-1]将字符串反转

if __name__ == '__main__':
    while True:#无限循环，以保证输入的数据位数正确以实现计算
        number = int(input("输入一个五位数:"))#输入一个五位数
        if len(str(number)) != 5:#判断是否为五位数
            print("输入错误，请重新输入：")#提示重新输入
        else:
            if hws(number):#判断是否为回文数 ---yes
                print("{}是回文数".format(number))#输出是回文数
                break#跳出循环
            else:# ---no
                print("{}不是回文数".format(number))#输出不是回文数
                break#跳出循环
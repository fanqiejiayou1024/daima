pd = input("是否是摄氏度？ 如果是输y,如果不是请输n：") #输入判断条件
if pd == "y": #判断是否为摄氏度
    c = eval(input()) #输入摄氏度
    print(1.8 * c + 32) #输出对应的华氏度
elif pd == "n": #判断是否为华氏度
    f = eval(input()) #输入华氏度
    print((f - 32) / 1.8) #输出对应的摄氏度
else: #输入错误
    print("输入错误") #输出错误
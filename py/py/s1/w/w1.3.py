a,b = 0,1 # 初始化a,b
while a < 1000: # 循环
    print(a,end=',') # 输出a
    a,b = b,a+b # 计算下一个值
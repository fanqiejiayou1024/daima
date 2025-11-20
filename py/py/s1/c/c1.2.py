n = input("请输入整数N：") # 输入整数N
sum = 0 # 初始化求和结果为0
for i in range(1, int(n)): # 循环从1到N-1
    sum += i + 1 # 每次循环，将1加到sum上
print("1到N求和结果：",sum) # 输出求和结果
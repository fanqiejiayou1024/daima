sum,tmp = 0,1 # 初始化sum tmp
for i in range(1,11): # 循环
    tmp = tmp * i # 计算tmp
    sum += tmp # 计算sum
print("运算的结果是：{}".format(sum)) # 输出sum
for i in range(1,10): # 循环：行
    for j in range(1,i+1): # 循环：列
        print("{}*{}={:2}".format(j,i,i*j),end=' ') # 格式化输出99乘法表
    print('') # 换行
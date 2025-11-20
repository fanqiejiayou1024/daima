n = 1 #初始化n
for i in range(4,0,-1): #倒序循环
    n = (n + 1) << 1 #n+1左移一位给n
print(n) #输出n
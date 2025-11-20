import turtle as t #导入turtle库，并取别名为s
t.speed(1024) #设置速度为1024
for i in range(5,206,3): #循环5到205，步长为3
    t.left(90) #左转90度
    t.fd(i) #前进i个dpi
t.left(90) #左转90度
t.done() #显示窗体
import turtle as t #导入turtle库，并取别名为s
for i in range(4): #循环四次
    t.pu() #画笔抬起
    t.fd(50) #画笔前进50dpi
    t.pd() #画笔落下
    t.fd(100) #画笔前进100dpi
    t.pu() #画笔抬起
    t.fd(50) #画笔前进50dpi
    t.pd() #画笔落下
    t.left(90) #左转90度
t.pu() #画笔抬起
t.goto(0,50) #画笔移动到(0,50)
t.pd() #画笔落下
t.right(90) #右转90度
t.done() #显示窗体
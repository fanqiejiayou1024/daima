import turtle as t #导入turtle库，并取别名为s
t.pu() #画笔抬起
t.goto(-121,0) #移动画笔到(-121,0)
t.left(30) #向左旋转30度
t.pd() #画笔落下
for i in range(3): #循环3次
    t.fd(210) #画一条210dpi的线
    t.right(90 + 30) #向右旋转90度+30度
t.pu() #画笔抬起
t.goto(121,0) #移动画笔到(121,0)
t.right(180) #向右旋转180度
t.pd() #画笔落下
for i in range(3): #循环3次
    t.fd(210) #画一条210dpi的线
    t.right(90 + 30) #向右旋转90度+30度
t.left(180) #向左旋转180度
t.pu() #画笔抬起
t.goto(-121,0) #移动画笔到(-121,0)
t.fd(70) #画一条70dpi的线
t.pd() #画笔落下
t.done() #显示窗格
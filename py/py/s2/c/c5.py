import turtle as t #导入turtle库，并取别名为s
for i in range(3): #循环3次
    t.fd(100) #前进100dpi
    t.right(90+30) #左转120度
t.pu() #抬起画笔
t.goto(-50,-87) #移动到坐标(-50,-87)
t.pd() #放下画笔
for i in range(3): #循环3次
    t.fd(200) #前进200dpi
    t.left(90+30) #右转120度
t.pu() #抬起画笔
t.goto(0,0) #移动到坐标(0,0)
t.pd() #放下画笔
t.done() #显示窗体
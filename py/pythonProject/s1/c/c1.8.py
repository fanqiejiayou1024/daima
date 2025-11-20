from turtle import * #导入turtle的全部
color("red","yellow") #设置颜色
begin_fill() #开始填充
while True: #循环
    forward(200) #前进200dpi
    left(170) #左转170度
    if abs(pos()) < 1: #判断是否到达原点
        break #到达原点跳出循环
end_fill() #填充结束
done() #结束不关窗口
from turtle import * #导入turtle的全部
fillcolor("red") #填充颜色为红色
begin_fill() #开始填充
while True: #循环
    forward(200) #前进200dpi
    right(144) #向右转144度
    if abs(pos()) < 1: #判断坐标是否小于1
        break #坐标小于1跳出循环
end_fill() #结束填充

done()
import turtle as t
import datetime as d
def drawGap():
    t.penup()
    t.fd(5)
def drawLine(draw):
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)
def drawDigit(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(20)
def drawDate(date):
    t.pencolor("red")
    for i in date:
        if i == "-":
            t.write("年",font=("Arial",18,"normal"))
            #t.pencolor("green")
            t.fd(40)
        elif i == "=":
            t.write("月",font=("Arial",18,"normal"))
            #t.pencolor("blue")
            t.fd(40)
        elif i == "*":
            t.write("日",font=("Arial",18,"normal"))
            #t.pencolor("red")
            t.fd(40)
        else:
            drawDigit(eval(i))
if __name__ == "__main__":
    t.setup(800,350,200,200)
    t.speed(100000000)
    t.penup()
    t.fd(-350)
    t.pensize(5)
    drawDate(d.datetime.now().strftime("%Y-%m=%d*"))
    t.hideturtle()
    t.done()
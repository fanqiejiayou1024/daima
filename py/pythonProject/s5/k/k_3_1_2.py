import turtle as t
def koch(size,n):
    if n==0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)
if __name__=='__main__':
    t.setup(600,600)
    t.speed(0)
    t.pencolor("green")
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(2)
    le = eval(input('请输入阶数：'))
    n = int(input('请输入层数：'))
    for i in range(n):
        koch(400,le)
        t.right(360 / n)
    t.hideturtle()
    t.done()
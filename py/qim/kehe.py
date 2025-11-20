import turtle as t
def kehe(size,n):
    if n == 0:
        t.fd(size)
    else:
        for i in [0,60,-120,60]:
            t.left(i)
            kehe(size/3,n-1)

if __name__ == '__main__':
    t.speed(0)
    t.setup(600,600)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(2)
    level = 5
    for i in range(2):
        kehe(400,level)
        t.right(120)
    kehe(400,level)
    t.hideturtle()
    t.done()

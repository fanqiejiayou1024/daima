import random as r

s = r.randint(0, 9)
c = int(input("请输入一个数字："))
while True:
    if c > s:
        print("猜大了")
    elif c < s:
        print("猜小了")
    else:
        print("猜对了")
        break

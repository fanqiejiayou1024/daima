import random as ra

a = input()
b = ra.randint(0, 60)
while True:
    if (a.isdigit()):
        t = int(a)

        break
    else:
        print("存在不包含的数字")
        a = input("输入一个数字")
if t > b:
    print("Too large")
elif t < b:
    print("Too small")
else:
    print("Guessed,Very Good!")

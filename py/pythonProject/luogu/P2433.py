import math as m

n = int(input())
if n == 1:
    print("I love Luogu!")
elif n == 2:
    print(2 + 4, 10 - 2 - 4)
elif n == 3:
    print(14 // 4)
    print(4 * (14 // 4))
    print(14 - 4 * (14 // 4))
elif n == 4:
    print("{:.3f}".format(500 / 3))
elif n == 5:
    print((260 + 220) / (12 + 20))
elif n == 6:
    print(m.sqrt(6 * 6 + 9 * 9))
elif n == 7:
    y = 100
    y += 10
    print(y)
    y -= 20
    print(y)
    print("0")
elif n == 8:
    r = 5
    pi = 3.141593
    print(2 * pi * r)
    print(pi * m.pow(r, 2))
    print(4 / 3 * pi * pow(r, 3))
elif n == 9:
    print(((((1 + 1) * 2) + 1 * 2) + 1) * 2)
elif n == 10:
    """
    设原有a个评测任务，而每分钟增加x个评测任务
    a + 30x = 30 * 8
    a + 6x = 6 * 10
    
    x = 7.5
    a = 15
    
    15 + 7.5 * 10 = ? * 10
    """
    print(m.ceil((15 + 7.5 * 10) / 10))
elif n == 11:
    """
    a = 5
    b = 8
    
    a-b = 3
    """
    print(100 / 3)
elif n == 12:
    print(ord("M") - ord("A") + 1)
    print(chr(ord("A") - 1 + 18))
elif n == 13:
    r1, r2 = 4, 10
    pi = 3.141593
    v = 4 / 3 * pi * pow(r1, 3) + 4 / 3 * pi * pow(r2, 3)
    print("{:.0f}".format(m.pow(v, 1 / 3)))
elif n == 14:
    """
    设课程定价需降低x元
    (110−x)(10+x)=3500
    
    x = 40 or 60
    """
    print(110 - 40)

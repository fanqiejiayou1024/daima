while True:
    q = eval(input("请输入金额：(例：1024)"))
    s = input("请输入币种：(例：cny)")
    if s == "cny":
        cn = q / 6
        print("{:.2f}".format(cn))
    elif s == "usd":
        us = q * 6
        print("{:.2f}".format(us))
    else:
        print("输入错误")
    c = input("是否继续？(e退出)")
    if c == "e":
        break
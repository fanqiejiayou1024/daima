# 计算温度转换的入口
def temp(v):
    if v[-1] in ["F", "f"]:
        c = (eval(v[0:-1]) - 32) / 1.8
        return str(c) + "C"
    elif v[-1] in ["C", "c"]:
        f = eval(v[0:-1]) * 1.8 + 32
        return str(f) + "F"
    else:
        return "输入错误"


# 主函数入口
if __name__ == '__main__':
    v = input()
    print(temp(v))

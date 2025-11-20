def gcd(a, b):# 最大公约数
    while b != 0:
        a, b = b, a % b# 辗转相除法的核心步骤：将 b 赋值给 a，将 a % b 赋值给 b
    return a# 返回 a

def lcm(a, b):
    return a * b // gcd(a, b)# 最小公倍数 用 a * b 整除 最大公约数

if __name__ == '__main__':
    a = int(input("请输入第一个整数: "))# 输入第一个整数
    b = int(input("请输入第二个整数: "))# 输入第二个整数
    print("最大公约数:", gcd(a, b))# 输出最大公约数
    print("最小公倍数:",lcm(a, b))# 输出最小公倍数
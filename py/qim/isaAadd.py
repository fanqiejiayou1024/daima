def idOdd(n):
    if n % 2 == 0:
        return False
    else:
        return True
if __name__ == '__main__':
    n = int(input("请输入一个整数："))
    if idOdd(n):
        print("{}是奇数".format(n))
    else:
        print("{}是偶数".format(n))
        
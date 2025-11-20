c1,c2,c3 = map(int, input("请输入三个数字，用空格分隔:\n").split())
paixu = [c1, c2, c3]
paixu.sort()
print(paixu[0], paixu[1], paixu[2])
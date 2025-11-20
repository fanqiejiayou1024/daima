a = float(input())
a *= 10
b = a / 1000
c = a / 100 % 10
d = a / 10 % 10
e = a % 10
b = int(b)
c = int(c)
d = int(d)
e = int(e)
print("{3}.{2}{1}{0}".format(b, c, d, e))

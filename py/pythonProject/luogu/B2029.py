import math

h, r = map(int, input().split())
pi = 3.14
v = pi * (r * r) * h
s = 20 * 1000
c = math.ceil(s / v)
print(c)

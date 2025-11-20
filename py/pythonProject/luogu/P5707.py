import math

s, v = map(float, input().split())

sj = math.ceil(s / v)  # 时间

gotime = (480 + 2880 - 10 - sj) % 1440  # 480是从0点到8点的分钟数,2880是0一天的分钟数,1440是半天的分钟数
h = str(gotime // 60).zfill(2)
m = str(gotime % 60).zfill(2)
print("{}:{}".format(h, m))

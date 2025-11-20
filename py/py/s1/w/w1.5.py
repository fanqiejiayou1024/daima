from datetime import datetime #从datetime导入datetime
now = datetime.now() #获取当前时间
print(now) #输出当前时间
print(now.strftime("%x")) #输出当前时间的日期部分
print(now.strftime("%X")) #输出当前时间的时间部分
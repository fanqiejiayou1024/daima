import time

scale = 50  # 定义进度条的长度
print("执行开始".center(scale // 2, '-'))  # 打印执行开始的信息，居中对齐

start_time = time.perf_counter()  # 记录开始时间

for i in range(scale + 1):  # 循环从 0 到 scale
    a = '*' * i  # 计算已填充的部分
    b = '.' * (scale - i)  # 计算未填充的部分
    c = (i / scale) * 100  # 计算完成的百分比
    elapsed_time = time.perf_counter() - start_time  # 计算已用时间
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, elapsed_time), end='')  # 打印进度条，格式化输出百分比、进度条和已用时间
    time.sleep(0.05)  # 暂停 0.05 秒，模拟任务执行的时间

print("\n" + "执行结束".center(scale // 2, '-'))  # 打印执行结束的信息，居中对齐

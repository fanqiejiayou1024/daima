import time

s = 100
print("Welcome to the JDT Calculator")

# 使用 time.process_time() 替代 time.clock() py3.8删除了
start_time = time.process_time()

for i in range(s + 1):
    a = '*' * i
    b = '.' * (s - i)
    c = (i / s) * 100
    elapsed_time = time.process_time() - start_time
    print('\r{:^3.0f}%[{}->{}]'.format(c, a, b), end='')
    time.sleep(0.05)

print('\n')

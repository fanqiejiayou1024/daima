def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# 测试
print(isPrime(7))  # 输出: True
print(isPrime(10))  # 输出: False
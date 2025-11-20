def multi(*args):
    result = 1
    for num in args:
        result *= num
    return result

# 测试
print(multi(2, 3, 4))  # 输出: 24
def isNum(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# 测试
print(isNum("123"))  # 输出: True
print(isNum("abc"))  # 输出: False
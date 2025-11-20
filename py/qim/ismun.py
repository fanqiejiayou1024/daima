def isNum(s):
    try:
        # 尝试将字符串转换为整数
        int(s)
        return True
    except ValueError:
        try:
            # 尝试将字符串转换为浮点数
            float(s)
            return True
        except ValueError:
            try:
                # 尝试将字符串转换为复数
                complex(s)
                return True
            except ValueError:
                return False

# 测试用例
i = input("请输入：")
print(isNum(i))
text = input("请输入一行字符: ")#输入一行字符
counts = {'字母': 0, '数字': 0, '空格': 0, '其他': 0}#定义统计字母数字空格和其他字符
for char in text:#遍历输入的字符串
    if char.isalpha():#判断是否是字母
        counts['字母'] += 1
    elif char.isdigit():#判断是否是数字
        counts['数字'] += 1
    elif char.isspace():#判断是否是空格
        counts['空格'] += 1
    else:
        counts['其他'] += 1
print(counts)#输出统计结果
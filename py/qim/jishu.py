def count_characters(input_string):
    # 初始化计数器
    english_count = 0
    digit_count = 0
    space_count = 0
    other_count = 0

    # 遍历输入字符串中的每个字符
    for char in input_string:
        if char.isalpha():
            english_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    # 输出结果
    print("英文字符: ",english_count,"个")
    print("数字字符: ",digit_count,"个")
    print("空格字符: ",space_count,"个")
    print("其他字符: ",other_count,"个")

# 从键盘读取一行字符
input_string = input("请输入一行字符: ")

# 调用函数进行统计
count_characters(input_string)

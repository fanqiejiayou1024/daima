def safe_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("输入内容必须为整数!")

number = safe_input("请输入一个整数: ")
print(f"你输入的整数是: {number}")
def print_tianzige():
    # 打印横线
    def print_horizontal():
        print('+---+---+')

    # 打印竖线
    def print_vertical():
        print('|   |   |')

    # 打印一行完整的田字格
    def print_row():
        print_horizontal()
        print_vertical()
        print_vertical()
        print_horizontal()

    # 打印整个田字格
    for _ in range(2):
        print_row()

print_tianzige()
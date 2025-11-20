import turtle as t #导入turtle库，并取别名为s


def c():
    t.circle(40, 80)  # 绘制半径为40的圆，角度为80度
    t.circle(-40, 80)  # 绘制半径-40的圆，角度为80度
if __name__=='__main__':
    t.setup(650, 350, 200, 200)  # 设置绘图窗口的大小和位置，窗口宽 650，高 350，窗口左上角在屏幕坐标 (200, 200) 处
    t.up()  # 提起画笔
    t.fd(-300)  # 向后移动300dpi
    t.down()  # 放下画笔
    t.pensize(25)  # 设置画笔大小为25dpi
    t.seth(-40)  # 设置画笔初始方向为-40度
    t.pencolor("pink")  # 设置画笔颜色为粉色
    c()  # 调用函数
    t.pencolor("orange")  # 设置画笔颜色为橙色
    c()  # 调用函数
    # 设置画笔颜色为绿色
    t.pencolor("green")
    c()  # 调用函数
    # 设置画笔颜色为蓝色
    t.pencolor("blue")
    c()  # 调用函数
    # 设置画笔颜色为青色
    t.pencolor("cyan")
    c()  # 调用函数
    t.fd(40)
    t.circle(20, 180)  # 绘制半径为 20 的圆，角度为 180 度
    t.fd(40 * 2 / 3)  # 向前移动 40 * 2/3dpi
    t.done()  # 显示窗格

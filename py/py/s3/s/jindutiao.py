def print_progress_bar(progress):
    bar_length = 20
    filled_length = int(bar_length * progress)
    bar = '+' * filled_length + '-' * (bar_length - filled_length)
    print(f"[{bar}]")

# 示例用法
print_progress_bar(0.5)  # 输出一半的进度条
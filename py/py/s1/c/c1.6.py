diet = ['西红柿', '花椰菜单', '黄瓜单', '牛排',"虾仁"] # 初始化数组，向内投5个菜
for x in range(0,5): # 循环行
    for y in range(0,5): # 循环列
        if x != y: # 排除自身
            print(diet[x],diet[y]) # 输出菜品组合
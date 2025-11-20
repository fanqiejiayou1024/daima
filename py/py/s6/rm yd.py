def remove_duplicates(lst):
    return list(set(lst))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
print(remove_duplicates(numbers))  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
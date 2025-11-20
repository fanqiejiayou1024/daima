def has_duplicates(lst):
    return len(lst) != len(set(lst))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(has_duplicates(numbers))  # 输出: False

numbers_with_duplicates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
print(has_duplicates(numbers_with_duplicates))  # 输出: True
# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]


def double_function(example):
    list_doubled = []
    for i in example:
        double = i * 2
        list_doubled.append(double)
    return list_doubled


print(double_function([1, 2, 3, 4, 5, 6]))

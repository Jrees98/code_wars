"""
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
"""


def reverse_seq(n):
    top = n
    rev = [top]
    while top > 1:
        i = top - 1
        rev.append(i)
        top -= 1
    return rev


print(reverse_seq(10))


def reverse_seq1(n):
    return list(range(n, 0, -1))


print(reverse_seq1(10))

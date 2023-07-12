def solution(string):
    rev_word = ''
    for i in range(len(string)-1, -1, -1):
        char = string[i]
        rev_word += char
    return rev_word


print(solution('Hello'))
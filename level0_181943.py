def solution(my_string, overwrite_string, s):
    answer = ''
    temp = len(my_string) - len(overwrite_string) - s
    if temp >=1:
        return ''.join(list(my_string)[:s]) + overwrite_string + ''.join(list(my_string)[s+len(overwrite_string):])
    else:
        return ''.join(list(my_string)[:s]) + overwrite_string

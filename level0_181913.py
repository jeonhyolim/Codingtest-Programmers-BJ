def solution(my_string, queries):
    answer = 0
    my_string_lst = list(my_string)
    for i in range(len(queries)):
        change_part = queries[i] # [2, 3]
        change_sec = my_string_lst[change_part[0]:change_part[1]+1]
        #print(change_sec)
        change_sec.reverse()
        change_sec = ''.join(change_sec)
        #print(change_sec)
        my_string_lst[change_part[0]:change_part[1]+1] = change_sec
        #print(''.join(my_string_lst))
        
        #print(my_string_lst)
    return ''.join(my_string_lst)
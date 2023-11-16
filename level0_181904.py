def solution(my_string, m, c):
    temp = []
    temp2 = []
    my_string_list = list(my_string)
    for i in range(0, len(my_string), m):
        temp.append(my_string_list[i:i+m])
    for i in range(len(temp)):
        #print(i)
        temp2.append(temp[i][c-1]) # temp[0][1], temp[1][1]
    #print(temp2)
    return ''.join(temp2)

print(solution("ihrhbakrfpndopljhygc", 4, 2))
print(solution("programmers",1 , 1))
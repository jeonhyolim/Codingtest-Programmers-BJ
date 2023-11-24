def solution(s):
    answer = ''
    s_list = s.split(" ")
    for i in range(len(s_list)):
        temp = list(s_list[i]) # list(unFollowed)
        for j in range(len(temp)):
            if j == 0 and str(temp[0]):
                temp[0] = temp[0].upper()
            elif str(temp[j]):
                temp[j] = temp[j].lower()
        if i != len(s_list)-1:
            answer += ''.join(temp) + ' '
        else:
            answer += ''.join(temp)
    return answer

print(solution("3people unFollowed me"))
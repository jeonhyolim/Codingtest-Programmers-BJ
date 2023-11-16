def solution(t, p):
    answer = 0
    str_list = []
    t_list = list(t)
    #print(t_list)
    for i in range(0, len(t)):
        if len("".join(t_list[i:i+len(p)])) == len(p): # "".join(list_name) : 문자열 리스트 변수로 변환 후 하나로 합치기
            str_list.append(int("".join(t_list[i:i+len(p)]))) 
    #print(str_list)
    for i in range(0, len(str_list)):
        if str_list[i]<= int(p):
            answer +=1
    return answer

print(solution("3141592","271"))
print(solution("500220839878","7"))
print(solution("10203","15"))
def solution(myString, pat):
    answer = 0
#    print(type())
    for i in range(len(myString)-len(pat)+1): # 길이 6, 3 => 4번 반복
        temp = myString[i:i+len(pat)]
       # print(temp)
        if temp == pat:
            answer += 1
    return answer
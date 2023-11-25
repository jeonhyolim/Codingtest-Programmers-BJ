def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        temp = babbling[i]
        print(temp)
        while len(temp) != 0:
            if temp[0] == "a":
                try:
                    temp.replace("aya", "")
                except:
                    break
            elif temp[0] == "y":
                try:
                    temp.replace("ye", "")
                except:
                    break
            elif temp[0] == "w":
                try:
                    temp.replace("woo", "")
                except:
                    break
            elif temp[0] == "ma":
                try:
                    temp.replace("ma", "")
                except:
                    break
            else:
                break
        answer += 1           
    return answer

print(solution(["aya", "yee", "u", "maa"]))

def solution(babbling):
    answer = 0
    #print(len(babbling))
    for i in range(len(babbling)):
        #print(babbling[i])
        temp = ''
        check = ''
        for j in range(len(babbling[i])): # 알파벳 하나씩 체크
            temp += babbling[i][j]
            if temp in ["aya", "woo"]:
               # print(temp)
                if len(temp) !=3: #다른 애가 앞에 깔려있음
                    check += temp[len(temp) -3] # 발음 가능한 단어의 가장 앞 알파벳 저장
                    temp = temp[:len(temp)-3]
                    temp = ''.join(temp)
                else:
                    check += temp[0]
                    temp = ''
            elif temp in ["ye", "ma"]:
                #print(temp)
                if len(temp) !=2:
                    check += temp[len(temp) -2] # 발음 가능한 단어의 가장 앞 알파벳 저장
                    temp = temp[:len(temp)-2]
                    temp = ''.join(temp)
                else:
                    check += temp[0]
                    temp = ''
       # print(check, temp)
        if any(word in check for word in ["aa", "yy", "ww", "mm"]):
            continue
     #   elif "yy" in check:
     #       continue
     #   elif "ww" in check:
     #       continue
     #   elif "mm" in check:
     #       continue
        else:
            if temp == '':
                answer += 1
                #print('통과')
    return answer
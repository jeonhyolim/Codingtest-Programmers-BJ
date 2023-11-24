def solution(s): # 	"110010101001"	
    answer = [0,0]
    s_list = list(s)
    while "1" != s_list:
        wo_0_s = '1' * s_list.count('1') # 111111
        answer[1]+= len(s_list)-len(wo_0_s) # 제거한 0의 개수
        #print(answer[1])
        wo_0_s = ''.join(wo_0_s) # 리스트 형태를 -> 문자열로 합침
        #print(wo_0_s)
        s_list = change_two(len(wo_0_s)) # 얘를 2진법 변환, # 110
        #print(s_list)
        answer[0] +=1
        #print('한번 끝')
    return answer

def change_two(n): # 입력 문자로 받고 -> return도 문자열로 해줌
   # n = int(n) # 문자 -> 숫자로 바꿈
    answer = []
    while n!= 0:
        answer.append(str(n%2)) # 나머지 (대신 거꾸로 쌓임, ["0","0", "1"])
        n = n//2 # 몫
    return ''.join(reversed(answer)) # 뒤짚어주고 하나로 합쳐줌
    

print(solution("1111111"))
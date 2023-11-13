a = list(input())

def make_list(a):
    temp =[]
    answer = []
    for i in range(len(a)):
        if a[i] != '+' and a[i] != '-': # 숫자인 경우
            temp.append(str(a[i]))
        elif a[i] == '+':
            answer.append(int(''.join(temp))) # 그 전까지 쌓아둔 숫자를 answer로 보내기
            temp = []
            answer.append(a[i])
        elif a[i] =='-':
            if i == 0:
                answer.append('-')
                continue
            answer.append(int(''.join(temp))) # 그 전까지 쌓아둔 숫자를 answer로 보내기
            temp = []
            answer.append(a[i])
    answer.append(int(''.join(temp))) # 마지막 숫자
    return answer

from collections import deque
a_list = make_list(a)
if type(a_list[0]) == int:
    a_list = deque(a_list)
    a_list.appendleft('+')
    a_list = list(a_list)


    
answer = 0
temp = 0
flag = False
for i in range(0, len(a_list),2): # 반복횟수, 2로 설정해서 계속 부호만 거침
    if flag == False:
        if a_list[i] == '+':
            answer += a_list[i+1]
        elif a_list[i] == '-':
            temp += a_list[i+1]
            flag = True
    elif flag == True:
        if a_list[i] == '+':
            temp += a_list[i+1]
        elif a_list[i] == '-':
            answer -= temp
            temp = a_list[i+1]
answer -= temp

print(answer)

# 책 풀이
equation = input().split('-')
answer = 0

for i in equation[0].split('+'):
    answer += int(i)

for i in equation[1:]:
    for j in i.split('+'):
        answer -=int(j)

print(answer)



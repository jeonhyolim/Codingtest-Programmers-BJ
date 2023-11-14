food =[1, 7, 1, 2]

def solution(food):
    temp = '' # i=0 일 때
    for i in range(1, len(food)):
        if food[i] ==1:
            pass
        elif food[i] % 2 == 1: # 홀수 개수인 경우 -> 하나 뺴고 저장
            temp += str(i)*((food[i]-1)//2) # food[i]가 음식 개수, i가 음식 번호
        else:
            temp += str(i)*((food[i])//2)
    front = sorted(temp)
    front = ''.join(front)
    back = sorted(temp, reverse=True)
    back = ''.join(back)
    return front + '0' + back

print(solution(food))
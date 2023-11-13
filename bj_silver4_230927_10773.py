n = int(input()) # 입력 받을 수

money = [int(input()) for _ in range(n)] # 여러 줄의 정수 입력 받기
#print(money)
return_money = []


def solution(n):
    for i in range(len(money)):
        if money[i] != 0:
            return_money.append(money[i])
            #print(return_money)
        else:
            return_money.pop()
            #print(return_money)
    return sum(return_money)

print(solution(n))
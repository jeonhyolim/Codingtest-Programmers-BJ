def solution(n):
    #print(13%10)
    village_use = []
    #print(131//10)
    for i in range(1,200):
        if i % 3 !=0:
            if '3' not in str(i):
                village_use.append(i)
    #print(village_use)
    return village_use[n-1]


# 사용하지 않는 숫자 : 3의 배수, 10으로 나누었을 때 나머지가 3인 애들, 30~으로 시작하는 애들 , 130 이런 애들
# 3 -> 4
# 6 -> 8 (6+2) 6//3 = 2, 
# 9 -> 14 (5) 9//3 = 3 (3,6,9), 12/13
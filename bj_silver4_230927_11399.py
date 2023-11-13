# 그리디 알고리즘, 정렬
n=int(input())

min_time= [*map(int,input().split())] # 띄어서 숫자 input으로 받음 예) 3 1 4 3 2

def solution(min_time):
    min_time = sorted(min_time)
    min_sum = 0
    for i in range(len(min_time)):
        min_sum += min_time[i]*(len(min_time)-i)
    return min_sum 

print(solution(min_time))
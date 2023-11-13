num = int(input())

num_list = [int(input()) for _ in range(num)] 

# 재귀 해결책 : 동적 프로그래밍으로의 구현 (Bottom-up 상향식)
def solution_2217(n):
    koong = [1,1,2,4]
    if n<4:
        return koong[n]
    else:
        for _ in range(4, n+1):
            koong.append(koong[-1]+koong[-2]+koong[-3]+koong[-4])
        return koong[n]

for i in range(num):
    print(solution_2217(num_list[i]))

# 재귀 해결책 : 동적 프로그래밍으로의 구현 (Top-down 하향식)
'''
dp = [0]*100
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
n=100
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
'''

# 재귀로 구현 -> 시간 오래 걸림
'''
def solution_2217(n):
    answer = []
    if n < 2:
        answer.append(1) 
    elif n == 2:
        answer.append(2)
    elif n == 3:
        answer.append(4)
    elif n > 3:
        answer.append(sum(solution_2217(n-1) + solution_2217(n-2) + solution_2217(n-3) + solution_2217(n-4)))
    return answer

for i in range(num):
    print(solution_2217(num_list[i])[0])
'''
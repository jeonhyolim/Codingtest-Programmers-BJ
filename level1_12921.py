n=10

def decimal(num):
    for i in range(2, num):
        if num % i == 0: # 소수가 아님
            return 0
    return 1

def solution_bf(n):
    answer = []
    for i in range(2, n+1):
        answer.append(decimal(i))
    return sum(answer)

# 시간초과 -> 에라스토스테네스의 체
def solution(n):
    a= [False,False] + [True]*(n-1)
    primes = []
    for i in range(2,n+1):
        if a[i]: # True인 경우만 수행
            primes.append(i)
            for j in range(2*i, n+1, i): # 소수채택외 그 아이의 배수들은 다 False로 바꾼다 (소수로 판단한 i만큼 간격 띄우면서 확인, 배수 중에 가장 작은게 2곱했을 때니까 2i)
                a[j]=False
    return len(primes)

print(solution(n))
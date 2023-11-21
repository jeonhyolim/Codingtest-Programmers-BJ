number = 10
limit = 3
power = 2

def divisor_count(n):
    count = 0
    for i in range(1, int(n**(1/2))+1): # 범위 축소 -> 1~n을 2로 나눈 수 => 1~n의 양의제곱근
        if n % i == 0:
            count += 1
            if i != n//i:
                count += 1
    return count


def solution(number, limit, power):
    answer = 0
    for i in range(number):
        temp = divisor_count(i+1)
        if temp > limit:
            temp = power
        answer += temp
    return answer

print(solution(number, limit, power))
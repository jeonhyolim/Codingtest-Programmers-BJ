# 투포인터- Q.2018
n = int(input())

n_list = list(range(n))

start = 0
end = n
answer = 0
while start < end:
    if sum(n_list[start:end]) > n:
        end -= 1
        print(f'현재 위치: {start}, {end}')
    elif sum(n_list[start:end]) < n:
        start +=1
        print(f'현재 위치: {start}, {end}')
    elif sum(n_list[start:end]) == n:
        print(f'합: {start}, {end}')
        answer += 1
        start += 1
        end += 1
        print(f'현재 위치: {start}, {end}')

print(answer)
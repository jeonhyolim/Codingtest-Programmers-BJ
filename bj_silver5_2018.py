n = int(input())

start = 1
last = 2

n_list = list(range(1, n+1))

answer = 0
while last < n+1:
    if sum(n_list[start:last]) < n:
        last += 1
        print(start, last)
    elif sum(n_list[start:last]) == n:
        print(n_list[start:last])
        answer += 1
        start += 1
    else: # > n
        last -= 1
        print(start, last)

print(answer)
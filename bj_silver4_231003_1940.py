n= int(input())
m = int(input())
n_list = [*map(int,input().split())] # n

n_list.sort()
answer = 0
start, end = 0, n-1
while start < end:
    if n_list[start] + n_list[end] > m:
        end -= 1
    elif n_list[start] + n_list[end] < m:
        start += 1
    elif n_list[start] + n_list[end] == m:
        answer +=1
        end -= 1
        start +=1

print(answer)

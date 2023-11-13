n =int(input()) 
n_sort = [int(input()) for _ in range(n)] # 한 줄에 한 개의 데이터

#print(n_sort)

# n_list = []
# for i in range(max(n_sort)+1):
#     n_list.append(0)

# 빈 리스트 만들기
max_value = max(n_sort)
min_value = min(n_sort)
n_list = [0] * (max_value - min_value + 1)

for i in n_sort: #[0,1,2, ...]
    n_list[i-min_value] += 1

#print(n_list)

for i in range(len(n_list)):
    if n_list[i] > 0:
        for _ in range(n_list[i]):
            print(i+min_value) #n_list.index(n_list[i]))

import sys
n = int(input())
count_sort = [0] * 10001
for i in range(n):
    count_sort[int(sys.stdin.readline())] +=1
for i in range(10001):
    if count_sort[i] != 0:
        for j in range(count_sort[i]):
            print(i)


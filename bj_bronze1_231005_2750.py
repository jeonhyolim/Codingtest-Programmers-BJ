# 버블 정렬
n= int(input())
n_list = [int(input()) for _ in range(n)]

count = n-1
for j in range(n-1):
    for i in range(count):
        if n_list[i] > n_list[i+1]:
            n_list[i], n_list[i+1] = n_list[i+1], n_list[i] # swap 연산 수행
        #print(f'{j}번째 루프의 {i} 번째 시행')
    j += 1
    count -= 1

for i in range(n):
    print(n_list[i])
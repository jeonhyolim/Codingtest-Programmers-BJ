n, m = map(int, input().split()) # 사람 수, 치킨 종류
arr = [list(map(int, input().split())) for _ in range(n)]

from itertools import combinations

nums = list(range(0,m)) # 치킨의 개수
combi = list(combinations(nums, 3)) # [(0,1,2), (0,1,,3) ...]
#print(combi)
answer = []

# 치킨 개수가 3개보다 적은 경우 대비
if m<3: 
    k = m
else:
    k = 3

for i in range(len(combi)): # (0,1,2)
    new_arr = []
    for j in range(k): # 열 뽑기 (치킨 수대로 반복)
        t_arr = [list(x) for x in zip(*arr)]
        new_arr.append(t_arr[combi[i][j]]) # 치킨 수에 맞게 뽑은 열 추가 (보통 3개)
    new_arr = [list(x) for x in zip(*new_arr)] # [[1, 2, 3], [6, 5, 4], [3, 2, 7], [4, 5, 6]]
    #print(new_arr)
    #new_arr_reshape = [] # np.reshape(new_arr, (n,k))
    #for i in range(n):
     #   new_arr_reshape.append()
    #print(new_arr)
    answer_can = []
    for i in range(n): # 사람 수
        answer_can.append(max(new_arr[i]))
    answer.append(sum(answer_can))

print(max(answer))
# 백준은 넘파이를 못쓴다
'''
import numpy as np
n, m = map(int, input().split()) # 사람 수, 치킨 종류
arr = [list(map(int, input().split())) for _ in range(n)]
arr = np.array(arr)

from itertools import combinations

nums = list(range(0,m)) # 치킨의 개수
combi = list(combinations(nums, 3)) # [(0,1,2), (0,1,,3) ...]
#print(combi)

answer = []
# 치킨 개수가 3개보다 적은 경우 대비
if m<3: 
    k = m
else:
    k = 3

for i in range(len(combi)): # (0,1,2)
    new_arr = []
    for j in range(k): # 열 뽑기 (치킨 수대로 반복)
        new_arr.append(np.array(arr).T[combi[i][j]]) # 치킨 수에 맞게 뽑은 열 추가 (보통 3개)
    new_arr = np.array(new_arr).T
    new_arr = np.reshape(new_arr, (n,k))
    #print(new_arr)
    answer_can = []
    for i in range(n):
        answer_can.append(max(new_arr[i]))
    answer.append(sum(answer_can))

print(max(answer))
'''

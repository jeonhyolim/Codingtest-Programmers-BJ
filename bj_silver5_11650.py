# 선택정렬을 통한 구현
n = int(input())
xy_arr = []
for _ in range(n):
    xy_arr.append([int(x) for x in input().split()])
#print(xy_arr)
'''
for j in range(n):
    # 가장 작은 값을 저장할 변수에 j를 초기화
    min_idx =j
    for i in range(j+1, n):
        if xy_arr[min_idx] > xy_arr[i]:
            min_idx = i 
        elif xy_arr[min_idx] == xy_arr[i]:
            if xy_arr[min_idx][1] > xy_arr[i][1]:
                min_idx = i
    xy_arr[j], xy_arr[min_idx] = xy_arr[min_idx], xy_arr[j]
#print(xy_arr)
'''

xy_arr = sorted(xy_arr)
for i in range(n):
    print(xy_arr[i][0], xy_arr[i][1])
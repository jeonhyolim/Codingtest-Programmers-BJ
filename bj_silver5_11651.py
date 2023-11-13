a = int(input())
arr = [list(map(int, input().split())) for _ in range(a)]
#arr = list(map(int, arr))
print(arr)
arr.sort(key=lambda x:(x[1], x[0]))
#print(arr)
for i in range(a):
    print(int(arr[i][0]), int(arr[i][1]))
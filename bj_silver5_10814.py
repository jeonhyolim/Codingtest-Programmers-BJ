a = int(input())
arr = [list(map(str, input().split())) for _ in range(a)]
#arr = list(map(int, arr))
print(arr)
arr.sort(key=lambda x:(int(x[0])))
#print(arr)
for i in range(a):
    print(int(arr[i][0]), str(arr[i][1]))
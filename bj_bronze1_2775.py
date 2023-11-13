T = int(input())
k=[]
n=[]
for i in range(T*2):
    if i == 0 or i %2==0:
        k.append(int(input()))
    else:
        n.append(int(input()))

#arr = [int(input()) for _ in range(T*2)]
#print(k)

def apt_living(n,k): # 호, 층
    arr = []
    for _ in range(k+1):
        line = []
        for _ in range(n):
            line.append(0)
        arr.append(line)
    #print(arr)

    for i in range(k+1): # 각 층의 0호 => 1명
        arr[i][0] = 1
    
    #print(arr)
    
    arr[0] = list(range(1, n+1))

    #print(arr)

    for i in range(1, k+1): # 호
        for j in range(1,n): # 층
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    return arr

for i in range(T):
    arr = apt_living(n[i], k[i])
    check = k[i] -1
    #print(check)
    print(sum(arr[check])) #[n[i]]))
n= int(input())

num = list(map(int, input().split()))

def gcd(i,j):
    if max(i,j) % min(i,j) == 0:
        return min(i,j)

    for k in reversed(range(min(i,j))):
        #print(k)
        if i % k == 0 and j % k == 0:
            return k


for i in range(n-1):
    gcd_num = gcd(num[0], num[i+1]) # 4
    print(f'{num[0]//gcd_num}/{num[i+1]//gcd_num}')

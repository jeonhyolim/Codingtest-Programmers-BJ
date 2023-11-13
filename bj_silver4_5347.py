n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

#print(arr)
def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd(a,b):
    if a <b: # a가 더 크다는 것을 가정하고
        a,b = b,a
    #print(a,b)
    while b!=0:
        r =a % b 
        #print(r)
        a = b
        if r == 0:
            return b
        else:
            b = r
            #print(a,b)
def lcm(a,b):
    return int(a*b/gcd(a,b))

for i in range(len(arr)):
    print(lcm(arr[i][0], arr[i][1]))



    
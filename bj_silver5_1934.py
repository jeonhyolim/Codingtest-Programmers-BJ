num = int(input())

num_list = [list(map(int, input().split())) for _ in range(num)]
#print(num_list)

def gcd(a,b):
    if a<b:
        a,b = b,a # a가 더 큰 값
    while b!=0:
        r = a % b
        a = b
        if r == 0:
            return b
        else:
            b = r

def lcm(a,b):
    gcd_ab = gcd(a,b)
    return gcd_ab * (a//gcd_ab) * (b//gcd_ab)

for i in range(num):
    print(lcm(num_list[i][0], num_list[i][1]))
   
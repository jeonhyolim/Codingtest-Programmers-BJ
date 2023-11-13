num = str(input())

num = num.split(':')
#print(num)

num = list(map(int, num))
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

gcd_num = gcd(num[0], num[1])
print(f'{num[0] // gcd_num}:{num[1]//gcd_num}')
    
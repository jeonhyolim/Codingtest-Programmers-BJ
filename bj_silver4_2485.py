n = int(input())
n_list = [int(input()) for _ in range(n)]

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 가로수 간격 계산
gcd_check = []
for i in range(len(n_list)-1): # 4
    gcd_check.append(n_list[i+1]-n_list[i])
    #gcd_check_set = list(set(gcd_check))
    #print(gcd_check)

# 가로수 간격들의 최대공약수
gcd_min = gcd_check[0]
for i in range(1, len(gcd_check)):
    gcd_min = gcd(gcd_min, gcd_check[i])

answer = []
for i in range(len(gcd_check)):
    answer.append((gcd_check[i]-gcd_min)/gcd_min)

print(int(sum(answer)))

'''
# 삼중 for문 => 시간 초과
def gcd(gcd_check): # list 형태로 들어옴
    gcd_list = []
    for i in range(0,len(gcd_check)-1):
        for j in range(1, len(gcd_check)):
            for k in (range(min(gcd_check[i], gcd_check[j]),0,-1)): 
                #print(gcd_check[i],gcd_check[j],k)
                if gcd_check[i] % k ==0 and gcd_check[j] % k == 0:
                    gcd_list.append(k)
                    break 
    #print(f'최대공약수 후보{gcd_list}')
    return min(gcd_list)
'''
'''
def gcd(a,b): # 두 개일 때
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
'''
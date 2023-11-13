a = list(map(int, input().split())) 
#print(a)

import math
A=a[0]
B= a[1]
V=a[2]
print(math.ceil((V-A)/(A-B)+1))

'''
# 시간 초과
now = 0
count = 0
while now < a[2]-1:
    now += (a[0]-a[1])
    count += 1

print(count)
'''
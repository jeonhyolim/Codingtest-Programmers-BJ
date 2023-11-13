n = int(input())
summ = 0
before_num = 0

if len(str(n)) == 1:
    print(n)
else: 
    # 반복되는 값
    for i in range(1, len(str(n))):
        #print(i)
        summ += i * (9*(10**(i-1)))
        before_num += 9*(10**(i-1))
    # 새로 생긴 값
    summ += len(str(n)) * (n-before_num)
    print(summ)



# 시간초과
'''
new_number = ''
for i in range(1, n+1):
    new_number += str(i)

print(len(new_number))
'''
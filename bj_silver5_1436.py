n = int(input())
answer = 0
check_number = 666
while n != answer:
    if '666' in str(check_number):
        answer += 1
        check_number += 1
    else:
        check_number +=1
print(check_number-1)


'''
n_list = []
for _ in range(n):
    n_list.append([int(x) for x in input().split()])

answer = [0] * n
for i in range(n):
    for j in range(n):
        #print(i, j)
        if i != j:
            if n_list[i][0] < n_list[j][0] and n_list[i][1] < n_list[j][1]:
                answer[i] +=1
#print(answer)

#rank = sorted(answer)

for i in range(n):
    print(answer[i]+1, end=' ')

#for i in range(n):
#    print(rank.index(answer[i])+1, end=' ')
'''
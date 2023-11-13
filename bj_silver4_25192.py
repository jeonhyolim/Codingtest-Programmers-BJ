n = int(input())
check = [input() for _ in range(n)]
#print(check)

#check.count('ENTER')

answer = 0
count = 0
name = []
for i in range(1,len(check)):
    if check[i] == 'ENTER':
        answer += len(set(name))
        name = []
    else:
        name.append(check[i])
answer += len(set(name))
print(answer)
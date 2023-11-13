# gcd -> 최대공약수
n = int(input())
question_list = []
for _ in range(n):
    question_list.append([int(x) for x in input().split()])

def gcd(a,b):
    for gcd in range(min(a,b), 0, -1): # range(start, stop, step)
        if a % gcd == 0 and b% gcd ==0:
            return gcd

def solution_9613(lst):
    answer = []
    start = 1
    for i in range(start, len(lst)-1):
        for j in range(start+1, len(lst)):
            print(f'{i}번째와 {j}번째')
            answer.append(gcd(lst[i], lst[j]))
        start +=1 
    print(answer)
    return sum(answer)

for k in range(n):
    print(solution_9613(question_list[k]))
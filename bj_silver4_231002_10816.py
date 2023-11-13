n = int(input())
n_number = [*map(int,input().split())]
m = int(input())
m_number = [*map(int,input().split())]
#print(n_number, m_number)

n_dict = {}

for i in range(len(n_number)):
    if str(n_number[i]) in n_dict.keys():
        n_dict[str(n_number[i])] += 1
    else:
        n_dict[str(n_number[i])] = 1

answer = []
for i in range(len(m_number)):
    if str(m_number[i]) in n_dict.keys():
        answer.append(n_dict[str(m_number[i])])
    else:
        answer.append('0')

for i in range(len(answer)):
    print(answer[i], end=' ')




'''
# 시간초과 list count 함수
for i in range(m):
    print(n_number.count(m_number[i]), end=' ')
'''
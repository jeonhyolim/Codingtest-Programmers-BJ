n, m = map(int, input().split())

solution = [str(input()) for _ in range(n+m)] 

name_dict = {}
answer = []
for i in range(n+m):
    if solution[i] in name_dict.keys():
        answer.append(solution[i])
    else:
        name_dict[str(solution[i])] = 1
print(len(answer))

answer.sort()

for i in range(len(answer)):
    print(answer[i])
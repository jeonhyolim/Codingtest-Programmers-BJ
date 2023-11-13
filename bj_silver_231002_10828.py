n = int(input())

solution = [str(input()) for _ in range(n)] 

#print(solution)

stack_list = []
for i in range(n):
    if solution[i].startswith('push'):
        stack_list.append(int(solution[i].split(' ')[1]))
    elif solution[i] == 'pop':
        if stack_list == []:
            print(-1)
        else:
            print(stack_list[len(stack_list)-1])
            stack_list= stack_list[:len(stack_list)-1]
    elif solution[i] == 'size':
        print(len(stack_list))
    elif solution[i] == 'empty':
        if stack_list == []:
            print(1)
        else:
            print(0)
    elif solution[i] == 'top':
        if stack_list == []:
            print(-1)
        else:
            print(stack_list[len(stack_list)-1])

'''
def solution_10828(stack_list):
    print(solution[0])
    answer = []
    for i in range(n):
        if solution[i].startswith('push'):
            stack_list.append(int(solution[i].split(' ')[1]))
        elif solution[i] == 'pop':
            if len(stack_list) == 0:
                answer.append(-1)
            else:
                answer.append(stack_list[len(stack_list)-1])
                stack_list= stack_list.pop(-1)
        elif solution[i] == 'size':
            answer.append(len(stack_list))
        elif solution[i] == 'empty':
            if len(stack_list) == 0:
                answer.append(1)
            else:
                answer.append(0)
        elif solution[i] == 'top':
            if len(stack_list) == 0:
                answer.append(-1)
            else:
                answer.append(stack_list[len(stack_list)-1])
        print(answer)
        return answer

for _ in range(n):
    print(solution_10828(stack_list))

'''
n = int(input())

solution = [list(map(int, input().split())) for _ in range(n)] 

#print(solution[1][0], solution[1][1])

stack_list = []
for i in range(n):
    if solution[i][0] ==1:
        stack_list.append(solution[i][1])
    elif solution[i] == [2]:
        if stack_list == []:
            print(-1)
        else:
            print(stack_list.pop())
            #print(stack_list) #[len(stack_list)-1])
    elif solution[i] == [3]:
        print(len(stack_list))
    elif solution[i] == [4]:
        if stack_list == []:
            print(1)
        else:
            print(0)
    elif solution[i] == [5]:
        if stack_list == []:
            print(-1)
        else:
            print(stack_list[len(stack_list)-1])
            
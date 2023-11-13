n = int(input())

solution = [str(input()) for _ in range(n)] 
deque_list = []
for i in range(n):
    if solution[i].startswith('push_front'):
        deque_list.insert(0, solution[i].split(' ')[1])
    elif solution[i].startswith('push_back'):
        deque_list.append(solution[i].split(' ')[1])
    elif solution[i] == 'pop_front':
        if len(deque_list) == 0:
            print(-1)
        else:
            print(deque_list[0])
            deque_list = deque_list[1:]
    elif solution[i] == 'pop_back':
        if len(deque_list) == 0:
            print(-1)
        else:
            print(deque_list[len(deque_list)-1])
            deque_list = deque_list[:len(deque_list)-1]
    elif solution[i] == 'size':
        print(len(deque_list))
    elif solution[i] == 'empty':
        if len(deque_list) == 0:
            print(1)
        else:
            print(0)
    elif solution[i] == 'front':
        if len(deque_list) == 0:
            print(-1)
        else:
            print(deque_list[0])
    elif solution[i] == 'back':
        if len(deque_list) == 0:
            print(-1)
        else:
            print(deque_list[len(deque_list)-1])

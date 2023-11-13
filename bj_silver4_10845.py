n = int(input())

solution = [str(input()) for _ in range(n)] 
que_list = []
for i in range(n):
    if solution[i].startswith('push'):
        #print(solution[i].split(' ')[1])
        que_list.append(solution[i].split(' ')[1])
        #print(f'넣어졌는지 확인 {que_list}')
    elif solution[i] == 'pop':
        if len(que_list) == 0:
            print(-1)
        else:
            print(que_list[0])
            que_list = que_list[1:]
    elif solution[i] == 'size':
        print(len(que_list))
    elif solution[i] == 'empty':
        if len(que_list) == 0:
            print(1)
        else:
            print(0)
    elif solution[i] == 'front':
        if len(que_list) == 0:
            print(-1)
        else:
            print(que_list[0])
    elif solution[i] == 'back':
        if len(que_list) == 0:
            print(-1)
        else:
            print(que_list[len(que_list)-1])
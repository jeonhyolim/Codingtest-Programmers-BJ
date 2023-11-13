n = int(input())

solution = [list(input()) for _ in range(n)] 
#print(solution)

stack_list = solution[0]
def solution_9012(stack_list):
    answer = []
    if stack_list[0] == '(':
        for i in range(len(stack_list)):
            if stack_list[i] == '(':
                answer.append('(')
                #print(answer, len(answer))
            elif stack_list[i] == ')':
                if len(answer) == 0:
                    return 'NO'
                elif answer[-1] == '(':
                    answer = answer[:len(answer)-1]
                else:
                    return 'NO'
        if answer == []:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'

for i in range(n):
    print(solution_9012(solution[i]))

'''
def solution_9012(solution):
    answer = []
    for i in range(len(solution)):
        if solution[i][0] == '(':
            if solution[i].count('(') == solution[i].count(')'):
                answer.append('YES')
            else:
                answer.append('NO')
        else:
            answer.append('NO')

    return answer

for i in range(n):
    print(solution_9012(solution)[i])
'''
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for m in range(len(commands)):
        i = commands[m][0]
        j = commands[m][1]
        k = commands[m][2]
        temp_array = array[i-1:j]
        #print(array)
        temp_array = sorted(temp_array)
        answer.append(temp_array[k-1])
    return answer

print(solution(array,commands))
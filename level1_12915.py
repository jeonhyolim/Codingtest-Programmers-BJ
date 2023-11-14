strings = ["sun", 'dvd', "bud", "car", 'avd']
n=1

def solution(strings, n):
    answer = []
    temp_list = [] # u, v, u, a, v
    for i in range(len(strings)):
        temp_list.append(list(strings[i])[n])

    temp_sort = sorted(temp_list) # a, u, u, v, v
    lsset_temp_sort = sorted(list(set(temp_sort)))# set인 애들 # a, u, v

    temp_answer = {}
    for i in range(len(lsset_temp_sort)): # 3
        for j in range(len(temp_list)): # 5
            if strings[j][n] == lsset_temp_sort[i]: # a
                if strings[j][n] not in temp_answer.keys():
                    temp_answer[strings[j][n]] = ([strings[j]])
                    #print(temp_answer)
                else:
                    temp_answer[strings[j][n]].append((strings[j]))  
    temp_answer = list(temp_answer.values()) # [['car'], ['sun', 'bud'], ['dvd', 'avd']]  
   # print(temp_answer)
    
    for i in range(len((set(temp_sort)))):
        if len(temp_answer[i])==1:
            answer.append(temp_answer[i][0])
        else:
            sorted_temp_answer = sorted(temp_answer[i])
            for j in range(len(sorted_temp_answer)):
                answer.append(sorted_temp_answer[j])
    return answer

print(solution(strings,n))
def solution(participant, completion):
    com_dict ={}
    answer = ''
    for i in range(len(completion)):
        if completion[i] in com_dict.keys():
            com_dict[completion[i]] += 1
        else:
            com_dict[completion[i]] = 1
    #print(com_dict)
    for i in range(len(participant)):
        if participant[i] in com_dict.keys():
            if com_dict[participant[i]] != 0:
                com_dict[participant[i]] -= 1
            else:
                answer += participant[i]
        else:
            answer += participant[i]
    return answer

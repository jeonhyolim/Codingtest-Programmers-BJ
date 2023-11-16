answers=[1,3,2,4,2,1,3,2,4,2,1,3,2,4,2,1,3,2,4,2]

def solution(answers):
    per1 = [1, 2, 3, 4, 5] * 2000
    per2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    per3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    temp1 = 0
    temp2 = 0
    temp3 = 0
    for i in range(len(answers)):
        if answers[i] == per1[i]:
            temp1 += 1
        if answers[i] == per2[i]:
            temp2 += 1
        if answers[i] == per3[i]:
            temp3 += 1
    answer = [temp1, temp2, temp3]
    #print(answer)
    if len(set(answer)) == 1:
        return [1,2,3]
    elif answer.count(max(answer)) == 2:
        a = [1,2,3]
        a.remove(answer.index(min(answer))+1)
        return a

    return [answer.index(max(answer))+1]

print(solution(answers))
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo= [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

def solution(name, yearning, photo):
    name_yearning={}
    answer = []
    for i in range(len(name)):
        name_yearning[name[i]] = yearning[i]
    for i in range(len(photo)):
        temp = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name_yearning.keys():
                temp += (name_yearning[photo[i][j]])
        answer.append(temp)
    return answer

print(solution(name, yearning, photo))
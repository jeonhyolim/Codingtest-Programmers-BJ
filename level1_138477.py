k=4
score=[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
# 런타임에러

def solution(k, score):
    answer = [score[0]]
    temp = [score[0]]
    for i in range(1, len(score)):
        temp.append(score[i])
        if len(temp) <= k:
            answer.append(min(temp))
        else:
            temp.remove(min(temp))
            #sorted_temp = sorted(temp, reverse=True)
            answer.append(min(temp))
    return answer

print(solution(k, score))
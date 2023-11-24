def solution(array):
    answer = []
    array_one = list(set(array))

    for i in range(len(array_one)): # {1,2,3,4}
        temp = int(array_one[i])
        answer.append(array.count(temp)) # 개수를 넣어줌
    if answer.count(max(answer)) > 1:
        return -1
    else:
        return array_one[answer.index(max(answer))] # [1,1,3,1]
print(solution([1,1,2,2]))
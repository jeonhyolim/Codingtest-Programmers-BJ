numbers = [2,1,3,4,1]	

def solution(numbers):
    answer = []
    for i in range(0, len(numbers)-1):
        for j in range(1, len(numbers)):
            if i != j:
                temp = numbers[i]+numbers[j]
                answer.append(temp)
    answer = sorted(set(answer))
    return answer

print(solution(numbers))
nums =[1,2,3,4]# [1,2,7,6,4]
from itertools import combinations
#list(combinations(nums, 3))

def decimal(num):
    for i in range(2, num):
        if num % i ==0:
            return 'N'
    return 'Y'

def solution(nums):
    answers = []
    answer = []
    combi = list(combinations(nums, 3))
    for i in range(len(combi)):
        answers.append(sum(combi[i]))
  #  print(answers)
    for i in range(len(answers)):
        answer.append(decimal(answers[i]))

    return answer.count('Y')

print(solution(nums))
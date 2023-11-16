def solution(myString):
    answer = []
    mystring_split = myString.split("x")
    for i in range(len(mystring_split)):
        answer.append(len(mystring_split[i]))
    return answer

print(solution("oxooxoxxox"))
print(solution("xabcxdefxghi"))
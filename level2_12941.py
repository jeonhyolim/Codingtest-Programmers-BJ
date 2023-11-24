def solution(A,B):
    answer = 0
    A_sort = sorted(A, reverse=True)
    B_sort = sorted(B, reverse=False)
    for i in range(len(A)):
        answer += A_sort[i]*B_sort[i]
    return answer

print(solution([1,4,2], [5,4,4]))
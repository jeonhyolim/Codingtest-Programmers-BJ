def change_2_count_1(n):
    change_2 = []
    while n!=0:
        change_2.append(n%2)
        n = n//2
    return change_2.count(1) #''.join(reversed(change_2))

def solution(n):
    answer = 0
    m = n
    count_1 = change_2_count_1(n)
    while change_2_count_1(m+1) != count_1:
        m+=1
        answer +=1
    return answer+n+1

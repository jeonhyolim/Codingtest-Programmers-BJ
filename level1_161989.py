def solution(n, m, section):
    answer = 0
    i=0
    while i < n:
        end = section[i]+m-1
        if end >= n:
                
        print(end)
        j = i 
        while section[j+1] < end:
            j+= 1
        else:
            answer += 1
            break
    i = j
    return answer

print(solution(8,4,[2,3,6]))
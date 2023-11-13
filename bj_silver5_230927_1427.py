n=int(input())

def solution(n):
    n_list = list(map(str, str(n)))
    n_list.sort(reverse=True)
    
    return ''.join(n_list)

print(solution(n))


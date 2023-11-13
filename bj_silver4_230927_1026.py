n=int(input())

a_array= [*map(int,input().split())] 
b_array= [*map(int,input().split())] 


def solution(a_array, b_array):
    a_sort = sorted(a_array, reverse=True)
    b_sort = sorted(b_array, reverse= False)
    print(a_sort, b_sort)
    summ = 0
    for i in range(len(a_array)):
        summ+= a_sort[i]*b_sort[i]
    return summ

print(solution(a_array, b_array))
n, k = map(int, input().split())

def make_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* make_factorial(n-1)

def make_fact_part(n,m):
    summ = 1
    for i in range(m):
        summ = summ * (n-i)
    return summ

if k > n:
    print(0) 
else:
    print(make_fact_part(n,k)//make_factorial(k))
a = int(input())

def factorial(a):
    if a == 0 or a==1:
        return 1
    else:
        answer = a*factorial(a-1)
        return answer

print(factorial(a))
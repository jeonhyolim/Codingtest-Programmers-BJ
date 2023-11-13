a, b= input().split()

a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

only_a = a_set-b_set
only_a = list(only_a)

if len(only_a)==0:
    print(0)
else:
    only_a.sort()
    print(len(only_a))
    for i in range(len(only_a)):
        print(only_a[i], end=' ')
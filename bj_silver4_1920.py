n = int(input())
a_n_list = list(map(int, input().split()))
a_n_dict = {}
for i in range(n):
    if a_n_list[i] not in a_n_dict.keys():
        a_n_dict[a_n_list[i]] = True
#print(a_n_dict)

m = int(input())
check =list(map(int, input().split()))

for i in range(m):
    if check[i] in a_n_dict.keys():
        print(1)
    else:
        print(0)

'''
# 시간 초과
n = int(input())
a_n =list(map(int, input().split()))
m = int(input())
check =list(map(int, input().split()))

for i in range(m):
    if check[i] in a_n:
        print(1)
    else:
        print(0)
'''
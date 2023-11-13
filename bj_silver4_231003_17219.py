n, m = map(int, input().split())

memo = [str(input()) for _ in range(n)] 
find_list = [str(input()) for _ in range(m)] 

dict_memo = {}
for i in range(n):
    dict_memo[memo[i].split()[0]] = memo[i].split()[1]
for j in range(m):
    print(dict_memo[find_list[j]])
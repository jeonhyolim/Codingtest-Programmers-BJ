n,m = map(int, input().split())
s = [input() for _ in range(n)] # 같은 경우 없음
check = [input() for _ in range(m)] # 같은 경우 있을 수도 있음

#print(s)
#print(check)

check_dict = {}
for i in range(m):
    if check[i] in check_dict.keys():
        check_dict[check[i]] += 1
    else:
        check_dict[check[i]] = 1

answer = 0
for i in range(n):
    if s[i] in check_dict.keys():
        #print(check_dict[s[i]])
        answer += check_dict[s[i]]

print(answer)


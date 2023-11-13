n, k= map(int, input().split())
n_list = [int(input()) for _ in range(n)] 
n_list.reverse()
answer = 0
#print(n_list)
for i in range(n):
    if n_list[i] > k: # pass
        pass
    else:
        #print('이제 나누기')
        #print(n_list[i],k)
        answer += k // n_list[i]
        k = k%n_list[i]
print(answer)
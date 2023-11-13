n, k= map(int, input().split())
k_list = [int(input()) for _ in range(n)]
k_list.reverse()
print(k_list)
coin_count = 0
i =0
if k_list[i] <= k:
    coin_count += k // k_list[i] # 몫
    print(coin_count)
    k = k % k_list[i] # 나머지
    print(k)
    i += 1
    #if i == n or k==0:
        #break
print(coin_count)

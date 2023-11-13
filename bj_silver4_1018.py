#import numpy as np
m, n= input().split()
arr = [list(input()) for _ in range(int(m))]
#arr = np.array(arr)
#print(arr)
wrong = 0
wrong_list = []
for i in range(int(m)-8+1): # 가로
    for j in range(int(n)-8+1): # 세로
        #print(i,j)
        check = [row[j:j+8] for row in arr[i:i+8]] #arr[i:i+8, j:j+8]
        #print(check)
        bw = ['B', 'W']
        for w in range(len(bw)):
            for a in range(0, len(check),2): # 짝수 (0,2,4,6)
                for b in range(0, len(check), 2): # (짝, 짝)
                    if check[a][b] != bw[w]:
                        wrong += 1
                for b in range(1, len(check), 2): # (짝, 홀)
                    if check[a][b] == bw[w]:
                        wrong += 1                
            for a in range(1, len(check),2): # 홀수 (1,3,5,7)
                for b in range(1, len(check), 2): # (홀, 홀)
                    if check[a][b] != bw[w]:
                        wrong += 1
                for b in range(0, len(check), 2): # (홀, 짝)
                    if check[a][b] == bw[w]:
                        wrong += 1        
            wrong_list.append(wrong)
            wrong = 0

print(min(wrong_list))




'''
#arr[0][0] =='W' # 0, 2, 4, => W: [짝수][짝수], [홀수][홀수]
wrong = 0
wrong_list = [] # for 문 여러 번 돌면 확인
for i in range(int(int(n)-8)): # 가로: 13-8+1
    for j in range(int(m)-8): # 세로: 3번: 10-8+1 (0에서부터 시작하니까 1 더하기 생략)
        print(i,j)
        check =arr[i:i+8, j:j+8] # 검사 범위
        print('======')
        print(check)
        if arr[0][0] =='W':
            for k in range(0,6,2):
                for b in range(0,6,2):
                    if k % 2 == 0 and b%2 ==0: # 둘 다 짝수
                        if check[k][b] != 'W':
                            wrong += 1 # 다시 칠해주어야 하는 애들
                        if check[k+1][b+1] != 'B':
                            wrong += 1
                        wrong_list.append(wrong)
                        #print(wrong)
                        wrong = 0
        elif arr[0][0] =='B':
            for k in range(0,8-1):
                for b in range(0,8-1):
                    if k % 2 == 0 and b%2 ==0: # 둘 다 짝수
                        #print(k,b)
                        if check[k][b] != 'B':
                            wrong += 1 # 다시 칠해주어야 하는 애들
                    else:
                        #print(k,b)
                        if check[k][b] != 'W':
                            wrong += 1
                        wrong_list.append(wrong)
                        #print(wrong)
                        wrong = 0

print(wrong_list)
 # 어차피 두 가지니까 -> [짝수][짝수]인 애들에서 W의 개수 세기, [홀수][홀수]인 애들에서 B의 개수 세기 (32에서 빼기 => 그게 잘못 칠한 애들)
'''
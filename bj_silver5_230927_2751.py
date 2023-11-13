n = int(input()) # 입력 받을 수

n_number = [int(input()) for _ in range(n)]
n_number = sorted(n_number)
#print(n_number)
for i in range(n):
    print(n_number[i])

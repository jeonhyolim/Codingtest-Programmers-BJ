n = int(input())

score =  [int(input()) for _ in range(n)] 
score = score[::-1]
print(score)
answer = 0
for i in range(0,n-1):
    if i == 0:
        print(f'시작 점수는 {score[i]}이야')
    while score[i] <= score[i+1]:
        print(f'한 단계 아래인 레벨이 {score[i+1]}점으로 {score[i]}보다 아직 크니까 1을 빼보자')
        score[i+1] -=1
        answer += 1
    print(f'한 단계 아래인 레벨이 {score[i+1]}점으로 {score[i]}보다 작으니까 넘어가')
    i+=1

print(answer)
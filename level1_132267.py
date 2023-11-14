a = 5 # 가져가야 하는 콜라 개수
b = 3 # 돌려주는 콜라의 개수가 여러 개인 경우
n = 21 # 주어진 콜라 수

# 틀렸던 이유 분석
# 1. b=1인 경우만 생각해서 -> 만약에 여러개이면 돌려줄 때도 배를 곱해주어야 하는 부분 놓침
# 2. 테스트케이스  12 -> 나머지가 0인 경우 판단 제대로

def solution(a, b, n):
    answer = 0
    while n >= a:
        if n % a == 0: #나머지가 0인 경우
            if n == a:
                n = (n//a)*b # 결론적으로 b
                answer += b
            else: # 6,3,18/ 2,1,10
                answer += b* (n // a) # 빈병 * 몫
                n = (n//a)*b
                print(answer)
        else: # 나머지가 생긴 경우
            answer += ((n-(n%a))//a) * b # (20-2) // 3 -> 6
            n = b* ((n-(n%a))//a) + (n%a)

    return answer

print(solution(a,b,n))
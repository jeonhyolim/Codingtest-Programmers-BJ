k = 4
m = 3 # 사과 개수
score =	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2] #[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

# 사과 상태 1~k점
# 사과 상자 가격 p*m (p는 사과들 중 가장 낮은 점수)

def solution(k, m, score):
    # 사과 상자 개수
    answer = 0
    box_num = len(score) // m
    sorted_score = sorted(score, reverse=True)
    standard = m-1 # 그 다음에 m씩 더하면서 확인
    for _ in range(box_num):
        answer += sorted_score[standard]
        standard += m
    #print(sorted_score)
   # while len(sorted_score) >= m:
   #     answer += sorted_score[m-1]
   #     sorted_score = sorted_score[m:]
        #print(sorted_score)
    return answer *m
print(solution(k, m, score))
#-,-,4, -,-,4,-,-,2,-,-,1
#[4, 4, 4, 4, 4, 4, 2, 2, 2, 2, 1, 1]
#2, 5, 8,11
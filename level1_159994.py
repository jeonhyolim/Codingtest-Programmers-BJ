cards1 =["i", "sadness", "sad"]#["you", "smarter"]#["list", "length", "important"]
cards2 = ["tired"] #["think", "more", "will", "be"]#["are", "very"]
goal = ["i", "sadness", "sad", "tired"] #["think", "more", "you", "will", "be", "smarter"] #["are", "very"]

# 정확도 64% => goal이 더 짧을 수도 있음  , 2 ≤ goal의 길이 ≤ cards1의 길이 + cards2의 길이
# 3,4,6,14,16,17 => # 어차피 소문자라 그랬으니까 대문자 넣어버리기
# 2, 10, 11 -> 런타임 에러 -> 시간초과로 추정 ~> try, except로 빨리 끝내버리기!
def solution(cards1, cards2, goal):
    for i in range(len(goal)):
        try:
            if goal[i] == cards1[0]:
                cards1 = cards1[1:]
                if len(cards1) == 0:
                    cards1 = ['A'] # 어차피 소문자라 그랬으니까 대문자 넣어버리기
            elif goal[i] == cards2[0]:
                cards2 = cards2[1:]
            else:
                return 'No'
        except:
            return 'No'

    return 'Yes'

print(solution(cards1, cards2, goal))
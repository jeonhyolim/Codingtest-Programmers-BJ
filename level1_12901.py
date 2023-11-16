a = 5
b = 24

# 조건 2월 29일까지 있음
# [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 2016년의 날들
# datetuime으로 풀어도됨 !!!

def solution(a, b):
    cal = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['THU','FRI','SAT','SUN','MON','TUE','WED']

    days = sum(cal[:a-1])+b # 1/1일과의 날짜 차이 받음
   # print(days)
    get = days % 7
    answer = week[get]
   # print(get)
    return answer

print(solution(a,b))
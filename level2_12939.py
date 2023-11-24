def solution(s):
    s= s.split(" ")
   # print(s)
    s = list(map(int, s))
   # print(s)
    return str(str(min(s)) + " " + str(max(s)))

print(solution("-1 -2 -3 -4"))
n = int(input())

answer = 0
if n <= 99:
    print(n)
elif n > 99 and n<111:
    print(99)
else:
    for i in range(111, n+1): # n인 자기 자신까지 봐야 하므로
        lst_n = list(str(i))
        #print(lst_n)
        if int(lst_n[1]) * 2 == int(lst_n[0]) + int(lst_n[2]): # 중간값이 앞뒤와 같다면
            answer += 1
    print(99+answer)

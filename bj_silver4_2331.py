a, p= map(int, input().split())

d_list = [a]

def next_number(n): # n은 숫자 int로 들어옴 예) 57
    split_number = []
    for _ in range(len(str(n))):
        split_number.append(n % 10) # 나머지
        n = n // 10
    answer = []
    for i in range(len(split_number)):
        answer.append(split_number[i]**p)
    return sum(answer)

while True:
    check = next_number(d_list[-1])
    if check in d_list:
        print(d_list.index(check))
        #print(check, len(d_list), d_list)
        break
    else:
        d_list.append(check)



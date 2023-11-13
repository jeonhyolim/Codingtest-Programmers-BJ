s = str(input())
def solution(s):
    s_array = []  # 사전에 쌓아둘 모든 접미사

    for i in range(len(list(s))):
        s_array.append(list(s)[i:])

    s_array_2 = []
    for i in range(len(s_array)):
        s_array_2.append(''.join(s_array[i]))
    
    return s_array_2


result = solution(s)

# 정렬해서 출력
for item in sorted(result):
    print(item)
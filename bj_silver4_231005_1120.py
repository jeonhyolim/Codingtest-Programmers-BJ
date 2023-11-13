a,b= map(str, input().split())

# 길이가 같으면 바로 비교
# 길이가 다르면 앞이나 뒤에 알파벳 추가
# A C B 이면 바로 0으로 끝내기

def difference_two_str(a, b):
    count = 0
    for i in range(len(a)):
        if list(a)[i] != list(b)[i]:
            count +=1
    return count

def difference_two_lst(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count +=1
    return count

a_list = list(a)
b_list = list(b)
answer = []

if str(a) in str(b):
    print(0)
elif len(a) == len(b):
    print(difference_two_str(a,b))
elif len(a) != len(b):
    check = len(a) # 우리가 확인해야 하는 애들의 최대 개수 (나머지는 껴맞출 수 있음)
    for j in range(len(b)-len(a)+1):
        #print(j)
        #print(difference_two_lst(a_list, b_list[j:j+check]))
        #print((a_list, b_list[j:j+check]))
        answer.append(difference_two_lst(a_list, b_list[j:j+check]))
    print(min(answer))
        
'''
# 문제 잘 못 이해!! a의 앞뒤에 넣는 것은 연결해서 넣어야 하는 것이 아님 @
def difference_two_lst(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count +=1
    return count

change_count = len(b)-len(a)-1 # a가 바뀌어야 하는 횟수
a_list = list(a)
b_list = list(b)

if str(a) in str(b):
    print(0)
elif len(a) == len(b):
    print(difference_two_str(a,b))
elif len(a) != len(b):
    # 1. a의 앞에 넣기
    a_list_front =  b_list[:len(b)-len(a)] +a_list
        
    # 2. a의 뒤에 넣기
    a_list_back = a_list + b_list[len(a):]
    print(min(difference_two_lst(a_list_front, b_list), difference_two_lst(a_list_back, b_list)))
    #print(b_list[:len(b)-len(a)], b_list[len(a):])
    #print(a_list_front, a_list_back)

이 프로그램은 1번 연산과 2번 연산을 각각 한 번 이상씩 사용할 때를 고려하고 있지 않은 것 같습니다.
'''
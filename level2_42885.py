def solution(people, limit):
    kg_people = sorted(people) # 가벼운 순으로 정렬
    answer = 0
    for i in range(len(kg_people)):
        if len(kg_people) == 0: # 다 태워서 내보냄 -> 끝
            return answer
        kg_left = limit - kg_people[-1] # 남은 몸무게
        kg_people = kg_people[:-1] # 1번 사람 내보냄
        answer += 1 # 구명 보트 하나 씀
        for j in reversed(range(len(kg_people))): # 무거운 사람부터 확인 !
            if kg_people[j] <= kg_left: # 두명 태울 수 있게 됨
                kg_people = kg_people[0:j] + kg_people[j+1:] # 2번쨰 사람 내보냄     
                break
    return answer

def solution(people, limit):
    kg_people = sorted(people, reverse= True) # 무거운 순으로 정렬
    ft_check = [False] * len(people) # 내리면 True로 바꿈
    answer = 0
    for i in range(len(kg_people)):
        if all(ft_check): # 다 태워서 내보냄 -> 끝
            return answer
        if ft_check[i] == True: # 내보낸 애는 넘어감
            continue
        kg_left = limit - kg_people[i] # 남은 몸무게
        ft_check[i] = True # 첫번쨰 사람 탐
        #print(ft_check)
        answer += 1 # 구명 보트 하나 씀
        for j in range(0,len(kg_people)): # 무거운 사람부터 확인 !
            if ft_check[j] == True:
                continue
            else:
                if kg_people[j] <= kg_left: # 두명 태울 수 있게 됨
                    ft_check[j] = True# 2번쨰 사람 내보냄   
                    #print(f'dddddd, {j}')
                    break
    return answer

def solution(people, limit):
    people_sort = sorted(people) # 작은 사람 순
    start = 0
    end = len(people)-1
    answer = 0
    while start <= end:
        if people_sort[start]+ people_sort[end] > limit: # 작은 애 못탐
            end -= 1
        elif people_sort[start]+ people_sort[end] <= limit: #둘다 탐
            start += 1
            end -= 1
        answer += 1

    return answer
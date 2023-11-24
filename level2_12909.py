from collections import deque
def solution(s):
    s_list = list(s)
    temp = deque()
    if s_list[0] == ')':
        return False
    else: # '(' 열리는 괄호로 잘 시작함
        temp.append(s_list[0])
        for i in range(1, len(s)): # 두번째 애부터 끝까지 순환
            if s_list[i] == '(': # 여는 괄호이면, 추가
                temp.append(s_list[i])
            else: # ')' 닫는 괄호이면 temp에서 '('를 빼줌
                if len(temp) == 0:
                    return False
                else:
                    print(temp)
                    temp.popleft()
        if len(temp) == 0:
            return True
        else:
            return False

print(solution("()()"))
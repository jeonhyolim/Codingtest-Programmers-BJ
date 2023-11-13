#n= int(input())
import sys
from collections import deque

n = int(sys.stdin.readline())

s = deque(list(range(1,n+1)))

while len(s) != 1:
    s.popleft()
    s.append(s.popleft()) # 두번째 아이
print(list(s)[0])


'''
### Solution1] 시간 초과 문제 발생, 리스트를 수정하는 과정이 연산 소모 많이 차지함
import sys
n = int(sys.stdin.readline())

s = list(range(1,n+1))

def solution(s):
    for _ in range(1, len(s)):        
        s= s[1:] # del s[0]
        s.insert(s[len(s)-1],s[0])
        s= s[1:] # del s[0]
    return s[0]

print(solution(s))

'''


'''
import sys
n = int(sys.stdin.readline())

s = list(range(1,n+1))

def solution(s):
    while len(s) != 1:
        for _ in range(1, len(s)):
            s= s[1:]
            s.insert(s[len(s)-1],s[0])
            s= s[1:]
        return s[0]

print(solution(s))
'''


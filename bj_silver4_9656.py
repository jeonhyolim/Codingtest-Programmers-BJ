from collections import deque
n = int(input())

turn = ['SK','CY'] * n
turn = deque(turn)
while n != 0:
    if n > 3:
        n -= 3
        turn.popleft()
    else:
        n -=1
        turn.popleft()
print(turn[0])
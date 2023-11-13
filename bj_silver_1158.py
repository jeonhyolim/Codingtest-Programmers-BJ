from collections import deque
n, k = map(int, input().split())

sitting = list(range(1,n+1))
sitting = deque(sitting)
#del sitting[k-1]
#out = [k]

out = []
for _ in range(1, n+1):
    sitting.rotate(-(k-1))
    out.append(sitting.popleft())    
    #print(sitting, out)
print(str(out).replace('[', '<').replace(']','>'))

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

'''
print(sorted(numbers)[k-1])
'''

#  퀵정렬로의구현, start // end

start = 0
end = n

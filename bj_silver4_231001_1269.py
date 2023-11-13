# 대칭차집합
a, b= map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a-b)+len(b-a))
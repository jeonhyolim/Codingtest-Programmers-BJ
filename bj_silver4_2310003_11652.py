import sys
num = int(sys.stdin.readline())

num_list = [str(input()) for _ in range(num)] 
num_dict = {}
for i in range(num):
    if num_list[i] in num_dict.keys():
        num_dict[num_list[i]] += 1
    else:
        num_dict[num_list[i]] = 1
answer = [k for k, v in num_dict.items() if max(num_dict.values()) == v]
answer = list(map(int, answer))

print(min(answer))

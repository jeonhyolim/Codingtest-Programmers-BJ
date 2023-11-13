n = int(input())
str_list = [input() for _ in range(n)]
str_dict = {}
for i in range(n):
    if str_list[i].split('.')[1] not in str_dict.keys():
        str_dict[str_list[i].split('.')[1]] = 1
    else:
        str_dict[str_list[i].split('.')[1]] += 1

sorted_dict = dict(sorted(str_dict.items(), key=lambda x: (x[0], -x[1])))
#print(sorted_dict)

for keys, value in sorted_dict.items():
    print(keys, value)
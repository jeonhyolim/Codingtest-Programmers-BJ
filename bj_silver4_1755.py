m, n = map(int, input().split()) 

print_num = list(range(m,n+1))

num_dict = {'0': 'zero', '1': 'one', '2':'two', '3':'three', '4':'four', '5':'five',
            '6':'six', '7':'seven', '8':'eight', '9':'nine'}

num_str = []
for i in range(len(print_num)):
    temp = str(print_num[i])
    temp_2= []
    for j in range(len(temp)):
        temp_2.append(num_dict[temp[j]])

    num_str.append(' '.join(temp_2))

#print(num_str, len(num_str))

answer = []
sorted_num_str = sorted(num_str)
for i in sorted_num_str:
    answer.append(num_str.index(i)+m)

count = 0

for i in range(len(answer)):
    print(answer[i] ,end=' ')
    count += 1

    if count == 10:
        print("")
        count = 0
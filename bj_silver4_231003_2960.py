n, m = map(int, input().split())

number_list = list(range(2,n+1))
del_list = []

while len(del_list) < m:
    #del_list.append(number_list[0]) # 소수 찾음
    for j in number_list:
        if j % number_list[0] ==0:
            del_list.append(j)
        else:
            pass
    #del_list = (list(set(del_list)))
    number_list = sorted(list(set(number_list) - set(del_list)))
    #print(f' 정렬:{number_list}')
#print(del_list, number_list)
print(del_list[m-1])




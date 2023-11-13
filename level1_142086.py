s= "foobar"
list_s = list(s)
answer = []
temp = []

for i in range(len(list_s)):
    if i == 0:
        answer.append(-1)
        temp.append(list_s[i])
    else:
        if list_s[i] in temp:
            reverse_temp = list(reversed(temp))
            answer.append(reverse_temp.index(list_s[i])+1)
            temp.append(list_s[i])
        else:
            answer.append(-1)
            temp.append(list_s[i])
print(answer)
str = input()
str_list = list(str)

for i in range(len(str_list)):
    if str_list[i].islower():
        str_list[i] = str_list[i].upper()
    else:
        str_list[i] = str_list[i].lower()
print(''.join(str_list))
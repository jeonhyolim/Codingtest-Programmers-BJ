s= "one4seveneight"
s_list = list(s)
temp = ''
num = []
num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
            'six':6, 'seven':7, 'eight':8, 'nine':9}
for i in range(len(s)):
    try:
        num.append(int(s_list[i]))
    except:
        temp += s_list[i]
        #print(temp)
        if temp in num_dict.keys():
            #print('smae')
            num.append(num_dict[temp])
            temp = ''
#print(num)
num = list(map(lambda x:str(x), num))
print(''.join(num))
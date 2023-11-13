n = int(input())
word = [str(input()) for _ in range(n)] 

def groupword(word): # 단어가 하나씩 들어옴
    word_list = list(word[0])
    for i in range(1, len(word)):
        if word[i] in word_list:
            if word[i] == word_list[-1]: # 같은 단어 연속임
                pass
            else:
                return 0 # 단어가 띄어서 또 나옴 'aba'
        else:
            word_list.append(word[i])
    return 1
summ =0
for i in range(len(word)):
    summ += groupword(word[i])

print(summ)
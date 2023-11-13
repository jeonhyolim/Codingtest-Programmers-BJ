n = int(input())
word_list = [str(input()) for _ in range(n)]
#print(word_list)

def good_bad_discriminator(word): # 'str': 예) 'ABAB'
    list_word =list(word)
    if len(word) % 2==1: #길이가 홀수이면
        return 0
    else: # 길이가 짝수이면
        if list_word.count('A') % 2 == 1 or list_word.count('B') % 2 == 1: # 만약 둘 중 하나라도 길이가 홀수이면
            return 0
        else: # A의 개수는 짝수, B의 개수도 짝수이라면
            word_left = []
            #print(word_left)
            for i in range(len(list_word)):
                if word_left == []:
                    word_left.append(list_word[i])
                    #print(f'비어있어서/처음이어서 reset하고 뒤에 애를 넣어줬더니 {word_left}가 되었고 {i}번쨰야')
                elif word_left[-1] == list_word[i]:
                    word_left.pop()
                    #print(f'둘이 같아서 같이 없애주어서 {word_left}가 되었어')
                elif word_left[-1] != list_word[i]:
                    word_left.append(list_word[i])
                    #print(f'둘이 달라서 새로 추가해서 {word_left}가 되었어')
            #print(f'최종적으로 남은 단어는 {word_left}')
            if len(word_left) > 1:
                return 0
            else:
                return 1
'''
            if 'ABA' in word:
                return 0
            elif 'BAB' in word:
                return 0
            else:
                return 1
'''

good_word_count = 0
for i in range(n):
    good_word_count += good_bad_discriminator(word_list[i])
print(good_word_count)


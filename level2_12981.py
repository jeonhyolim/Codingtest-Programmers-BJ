def solution(n, words):
    # 반환 형태 [탈락자 번호, 탈락자가 말한 단어 개수] , [나머지, 몫+1]
    word_check = [words[0]]
    for i in range(1, len(words)): #
        bf_word = word_check[-1]
        if bf_word[-1] != words[i][0]: # 단어가 이어지지 않음
            # 멈추기
            long = len(word_check)+1 # 틀린 단어까지 나온 단어 길이
            #print(long)
            if long%n ==0: # 마지막 사람인 경우
                return [n-long%n, (long // n)]
            else:
                return [long%n, (long // n)+1]
        else:
            if words[i] in word_check: # 똑같이 나왔을 때 멈추고
                long = len(word_check)+1 # 틀린 단어까지 나온 단어 길이
                #print(long)
                if long%n ==0:
                    return [n-long%n, (long // n)]
                else:
                    return [long%n, (long // n)+1]
            else:
                word_check.append(words[i])

    return [0,0] # 끝말잇기가 잘 끝난 경우
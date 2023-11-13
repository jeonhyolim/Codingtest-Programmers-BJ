n, m = map(int, input().split()) # 수, 문자열의 길이
dna = [list(input()) for _ in range(n)]
dna = sorted(dna) # 그러한 DNA가 여러개일떄는 사전출력

#print(dna)

if m ==1:
    count = 0
    max_dna = max(dna, key = dna.count)
    print(max_dna[0])
    for i in range(n):
        if dna[i] != max_dna:
            count += 1    
    print(count)
else:
    dna_transpose = [list(x) for x in zip(*dna)]
    dna_transpose = sorted(dna_transpose)
    #print(dna_transpose, len(dna_transpose))

    answer_dna=''
    for i in range(m):
        answer_dna += max(dna_transpose[i], key=dna_transpose[i].count)

    print(answer_dna)

    answer = 0
    for i in range(m):
        for j in range(n):
            if dna_transpose[i][j] != answer_dna[i]:
                answer += 1
    print(answer)

# 문제 잘못이해함
'''
answer = []
count = 0
for i in range(n):
    target = list(dna[i])
    for j in range(n):
        if i != j: # 둘이 같으면 자기자신이니까 넘어감
            temp = list(dna[j])
            print(temp, target)
            for k in range(m):
                if target[k] != temp[k]:
                    count += 1
                else:
                    print(target[k], temp[k])
    answer.append(count)
    count = 0
print(answer)
'''
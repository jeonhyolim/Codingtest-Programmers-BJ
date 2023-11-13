n = int(input()) # 입력 받을 수

book = [str(input()) for _ in range(n)] # 여러 줄

def solution_1302(book):
    book_count = dict()
    for i in book:
        if i not in book_count.keys():
            book_count[i]=1
        else:
            book_count[i]+=1
    #print(book_count) # {'top': 4, 'kimtop': 1}
    # 최대 반환
    max_book_list = [k for k, v in book_count.items() if max(book_count.values()) == v]
    max_book_list.sort()
    return max_book_list[0]

print(solution_1302(book))

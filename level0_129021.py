def solution(A, B):
    if A==B:
        return 0
    front = A[-1] # 문자 1개
    back = A[:len(A)-1] # 나머지
    count = 1
    #print(front+back)
    if back + front ==B:
        return 1
    else:
        for i in range(1, len(A)):
            front_temp = back[-1]
            back_temp = front + back[:len(back)-1]
            front = front_temp
            back = back_temp
            #print(back+front, back+front=="ohell")
            if back + front == B:
                #print(back+front, i)
                return count
            else:
                count += 1        
    return -1
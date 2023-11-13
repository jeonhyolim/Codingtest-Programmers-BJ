# 1235_silver4_학생번호
n = int(input()) 

student = [list(input()) for _ in range(n)]
for i in range(n):
    student[i]=list(reversed(student[i]))

#print(student)

def solution_1235(student):
    for i in range(len(student[0])):
        student_number = []
        for j in range(n): # 학생 번호 길이
            if student[j][:i+1] not in student_number: # if 'a' in  ['a','b','c']:
                # 번호가 겹치지 않는다면
                student_number.append(student[j][:i+1])
            if len(student_number) == n:
                return i+1
                #print(len(student_number))
            #i += 1
print(solution_1235(student))

'''
def solution_1235(student):
    new_student = []
    for i in range(len(student)):
        new_student.append(sorted(list(student[i]), reverse=True)) # new_student.append(list(student[i]).reverse()) 
    print(new_student)
    # new_student # [[1, 2, 3], [3, 1, 3]] ... 첫번째 애를 중심으로 해서 비교
    count= 0
    for row in range(len(new_student[0])):
        check_list = []
        check_list = [row[count] for row in new_student]
        #print(check_list, type(check_list))
        if len(check_list) == len(set(check_list)):
            print(count) # 길이 같음 -> 숫자가 다 다름
        else:
            count+=1 # 이렇게 풀면 안되는 듯.. 왜냐면

print(solution_1235(student))
'''

"""
def solution_1235(student):
    new_student = []
    for i in range(len(student)):
        new_student.append(sorted(list(student[i]), reverse=True)) # new_student.append(list(student[i]).reverse()) 
    print(new_student)
    # new_student # [[1, 2, 3], [3, 1, 3]] ... 하나씩 순서에 맞게 비교하기
    count= 0
    for row in range(len(new_student[0])):
        check_list = []
        check_list = [row[count] for row in new_student]
        #print(check_list, type(check_list))
        if len(check_list) == len(set(check_list)):
            print(count) # 길이 같음 -> 숫자가 다 다름
        else:
            count+=1 # 이렇게 풀면 안되는 듯.. 왜냐면

print(solution_1235(student))
"""
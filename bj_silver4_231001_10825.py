# 여러 개 + 여러 줄 입력
n = int(input())

students = []

for _ in range(n):
    name, s1, s2, s3 = input().split()
    students.append([name, s1, s2, s3]) # 리스트 형태로 받아서 넣기
#print(students) # [('k', '1', '2', '0'), 국어, 영어, 수학

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

#print(students)
for i in range(len(students)):
    print(students[i][0]) # 이중 리스트에서 앞에 해당 하는 이름만 출력


"""
for _ in range(n):
    name, s1, s2, s3 = input().split()
    students.append((name, int(s1), int(s2), int(s3)))
print(students) # [('k', '1', '2', '0'), 국어, 영어, 수학

sort_student = sorted(students, key=lambda x: (-x[1], x[2], x[3]))

for i in sort_student:
    print(i)
"""





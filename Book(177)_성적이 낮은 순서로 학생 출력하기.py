'''입력예시
2
홍길동 95
이순신 77
'''

n = int(input())
student = {}

for i in range(n):
    name,grade = input().split()
    student[name] = int(grade)

student = dict(sorted(student.items(), key=lambda x:x[1]))

for i in student.keys():
    print(i,end=' ')
'''입력예시
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''

import sys
n = int(input())

student = {}
for i in range(n):
	name,kor,eng,math = sys.stdin.readline().rstrip().split()
	student[name] = [int(kor),int(eng),int(math)]

student = dict(sorted(student.items(), key=lambda x:x[0]))
student = dict(sorted(student.items(), key=lambda x:-x[1][2]))
student = dict(sorted(student.items(), key=lambda x:x[1][1]))
student = dict(sorted(student.items(), key=lambda x:-x[1][0]))

for i in student.keys():
    print(i)
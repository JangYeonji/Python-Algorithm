'''
ZZZZZ 36
'''

import sys
input_data = sys.stdin.read().rsplit()

N = input_data[0]
B = int(input_data[1])

arr = []
mult = 1
sum_= 0
arr.append(1)

for i in range(len(N)-1):
    mult *= B
    arr.append(mult)

def switch(c):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,'Y':34,'Z':35}[c]

for x,y in zip(N[::-1],arr):
    sum_ += switch(x)*y

print(sum_)
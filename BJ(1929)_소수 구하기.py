'''입력 예제
3 16
'''

import math
n,m = map(int,input().split())
array = [True for i in range(m+1)]
array[0],array[1] = 0,0   #0,1은 소수 아님 주의

for i in range(2,int(math.sqrt(m))+1):
    if array[i]==True:
        j = 2
        while i*j <= m:
            array[i*j] = False
            j += 1

for i in range(n, m + 1):
    if array[i]:
        print(i)
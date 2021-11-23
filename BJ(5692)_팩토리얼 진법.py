'''입력 예제
719
1
15
110
102
0
'''
import sys

def fac(n):
    if n<=1:
        return 1
    return n * fac(n-1)

while True:
    result = 0
    n = sys.stdin.readline().rstrip()
    if n=='0':
        break
    for kdx, k in enumerate(n[::-1]):
        result += fac(kdx+1) * int(k)
    print(result)
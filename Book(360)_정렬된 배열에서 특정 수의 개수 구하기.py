'''입력 예시
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
'''

from bisect import bisect_left, bisect_right
n,x = map(int, input().split())
num = list(map(int,input().split()))

left = bisect_left(num,x)
right = bisect_right(num,x)

result = right-left

if result==0:
    print(-1)
else:
    print(result)
'''
7 2
1 1 2 2 2 2 3 

7 4
1 1 2 2 2 2 3
'''

import sys
input_data = sys.stdin.readline().rstrip()
n = int(input_data.split()[0])
x = int(input_data.split()[1])
array = list(map(int,input_data.split()[2:]))

def solution(start, end, x, array):
    cnt = 0
    while(start <= end):
        mid = int((start + (end - 1)) // 2)
        if array[mid]==x:
            cnt += 1
            del array[mid]
            end -= 1
        elif array[mid]>x:
            end = mid-1
        elif array[mid]<x:
            start = mid+1
    if cnt==0:
        return -1
    else:
        return cnt

solution(0,n,x,array)
'''
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
'''


import sys
input_data = sys.stdin.readline().rstrip()

n = int(input_data.split()[0])
array = list(map(int,input_data.split()[1:]))
def solution(start, end, array):
    while(start<=end):
        mid = (start + end) // 2
        if mid==array[mid]:
            return mid
        elif mid>array[mid]:
            start = mid+1
        elif mid<array[mid]:
            end = mid-1
    return -1

solution(0,n-1,array)
solution(0,n,array)
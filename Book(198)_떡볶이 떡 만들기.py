'''
4 6
19 15 10 17
'''

import sys
input_data = sys.stdin.readline().rstrip()

m = int(input_data.split()[1])
rice_cake = list(map(int,input_data.split()[2:]))
def solution(m,rice_cake):
    start = 0
    end = max(rice_cake)
    while(start<=end):
        mid = int((start + end) // 2)
        rice_sum = 0
        for i in rice_cake:
            if i>mid:
                rice_sum += i-mid
        if rice_sum == m:
            return mid
        elif rice_sum>m:
            start = mid+1
        elif rice_sum<m:
            end = mid-1
    return mid

solution(m,rice_cake)
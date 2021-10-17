'''
5
8 3 7 9 2
3
5 7 9
'''

import sys
input_data = sys.stdin.readline().rstrip()
m = int(input_data.split()[6])
n = int(input_data.split()[0])
m_array = sorted(list(map(int,input_data.split()[7:10])))   #m_array.sort()도 가능
n_array = sorted(list(map(int,input_data.split()[1:6])))

def solution(n_array,target,start,end):
    mid = (start+end)//2

    if start>end:
        return print('no',end = ' ')
    if i==n_array[mid]:
        return print('yes',end = ' ')
    elif i < n_array[mid]:
        solution(n_array,m_array,start,mid-1)
    elif i > n_array[mid]:
        solution(n_array,m_array,mid+1,end)
    else:
        return print('no',end = ' ')

for i in m_array:
	solution(n_array,i,0,n-1)
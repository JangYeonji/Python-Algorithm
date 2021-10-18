'''
719
1
15
110
102
0
'''

import sys
input_data = list(sys.stdin.readline().rstrip().split()[:-1])
answer = [0]*len(input_data)

def solution(n, array):
    sum_ = 0
    if n<1 or array=='':
        return 0
    for i in range(n)[::-1]:
        sum_ += (i+1) * int(array[0])
    array = array[1:]
    return sum_ + solution(n-1, array)

for idx, i in enumerate(input_data):
    answer[idx] = solution(len(i),i)
    try:
        if i[-2]>'0':
            answer[idx] -= 1
        print(answer[idx])
    except:
        print(answer[idx])
        continue
#mine

'''
5
abcde

3
zzz

1
i
'''

import sys
input_data = sys.stdin.readline().rstrip()
L = int(input_data.split()[0])
S = input_data.split()[1]

hash = dict()

for idx, i in enumerate(range(ord('a'),ord('z')+1)):
    hash[chr(i)] = idx+1

r = 31

sum_ = 0

for idx,i in enumerate(S):
    sum_ += hash[i] * (r**idx)

print(sum_ % 1234567891)
'''입력 예시
4 6
a t c i s w
'''
from itertools import combinations

l,c = map(int, input().split())
alpha = input().split()
alpha.sort()

result = list(combinations(alpha,l))

for idx in range(len(result)):
    result[idx] = ''.join(result[idx])
    leng = l
    if 'a' in result[idx]:
        leng -= 1
    if 'e' in result[idx]:
        leng -= 1
    if 'i' in result[idx]:
        leng -= 1
    if 'o' in result[idx]:
        leng -= 1
    if 'u' in result[idx]:
        leng -= 1
    if leng>=2 and leng<=(l-1):    
        print(result[idx])
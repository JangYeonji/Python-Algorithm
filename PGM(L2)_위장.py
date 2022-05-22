from collections import defaultdict
from functools import reduce   

def solution(clothes):
    tmp = 0
    answer = 0
    answer += len(clothes)
    hashs = defaultdict(int)
    for name,kind in clothes:
        hashs[kind] += 1
    if len(hashs) > 1:
        tmp = reduce(lambda x, y: x * y, hashs.values())
        
    return answer+tmp
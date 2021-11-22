from itertools import permutations
from math import sqrt

def solution(numbers):
    s = set()
    for i in range(1,len(numbers)+1):
        for a in permutations(numbers,i):
            s.add(a)
    li = set(map(''.join,s))
    li2 = set(map(''.join,s))
    li = set(map(int,li))
    li2 = set(map(int,li))
    for i in li:
        if i==1 or i==0:
            li2.remove(i)
        else:
            for k in range(2,int(sqrt(max(li)))+1):
                if i%k==0 and i!=k:
                    li2.remove(i)
                    break
    return len(li2)
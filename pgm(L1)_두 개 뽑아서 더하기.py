from itertools import combinations, permutations
def solution(numbers):
    s = set()
    num = set(combinations(numbers,2))
    
    for i in num:
        s.add(sum(i))

    return sorted(list(s))
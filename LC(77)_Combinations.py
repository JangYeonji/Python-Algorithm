from itertools import combinations, permutations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        li = []
        for i in range(1,n+1):
            li.append(i)
        
        return list(combinations(li,k))
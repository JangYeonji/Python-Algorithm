from itertools import permutations, combinations
import math
def solution(nums):
    answer = 0
    unique = [True] * (sum(nums)+1) 
    
    for i in range(2, int(math.sqrt(sum(nums)))+1):
        j = 2
        while i*j <= sum(nums):
            unique[i*j] = False
            j += 1
    
    combi = list(combinations(nums,3))
    
    for idx in range(len(combi)):
        combi[idx] = sum(combi[idx])
    
    for c in combi:
        if unique[c]:
            answer += 1
            
    return answer
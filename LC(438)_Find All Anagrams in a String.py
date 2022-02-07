from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lens = len(s)
        lenp = len(p)
        Cp = Counter(p)
        answer = []
        
        for i in range(lens-lenp+1):
            if Counter(s[i:i+lenp]) == Cp:
                answer.append(i)
                
        return answer
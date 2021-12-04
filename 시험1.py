#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
from collections import defaultdict
class Solution:
    def solution(self, number, dictionary):
        h = defaultdict(list)
        for i in sorted(dictionary):
            h[len(i)].append(i)
        answer = ''
        for n in number[:-1]:
            answer += ''.join(h[int(n)][0]) + ' '
            h[int(n)].pop(0)
        answer += ''.join(h[int(number[-1])][0])
        
        return answer
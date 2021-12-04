#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, X, Y, walkTime, sneakTime):
        if X==0 and Y==0:
            return 0
        elif X==0 or Y==0:
            if X!=0:
                return min(walkTime,sneakTime) * X
            else:
                return min(walkTime,sneakTime) * Y
        
        if walkTime == sneakTime:
            return sneakTime*Y
        elif walkTime*2 < sneakTime:
            return (X+Y)*walkTime
        elif walkTime*2 > sneakTime:
            return (sneakTime*Y) + ((X-Y)*walkTime)
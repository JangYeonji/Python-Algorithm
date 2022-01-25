class Solution:
    def climbStairs(self, n: int) -> int:
        answer = []
        answer.append(1)
        answer.append(2)
        
        for i in range(2,n):
            answer.append(answer[i-2]+answer[i-1])
        
        return answer[n-1]
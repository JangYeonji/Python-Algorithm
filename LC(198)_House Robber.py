class Solution:
    def rob(self, nums: List[int]) -> int:
        answer = []
        
        if len(nums)==1:
            return nums[-1]
        answer.append(nums[0])
        answer.append(max(nums[0], nums[1]))
        
        for i in range(2,len(nums)):
            answer.append(max(answer[i-1], answer[i-2]+nums[i]))
            
        return answer[-1]
from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if target in nums:
            a = bisect_left(nums,target)
            b = bisect_right(nums,target)
            
            return [a,b-1]
        
        return [-1,-1]
        
        
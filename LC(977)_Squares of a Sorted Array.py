import numpy as np
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = np.array(nums) ** 2
        answer.sort()
        return list(answer)
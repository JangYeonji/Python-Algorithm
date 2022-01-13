from bisect import bisect_right, bisect_left
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = bisect_right(numbers,target)
        answer = []
        for i in range(index):
            if target - numbers[i] in numbers:
                answer.append(i+1)
                answer.append(bisect_right(numbers,target-numbers[i]))
                if len(answer)==2:
                    break
                
        if answer == []:
            index = bisect_left(numbers,target)
            for j in numbers[index:]:
                if target - numbers[j] in numbers:
                    answer.append(j+1+index)
                    answer.append(numbers.index(target-numbers[i])+1+index)
        return answer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        
        while end-start > 0:
            if numbers[end] + numbers[start] == target:
                return [start+1,end+1]
            elif numbers[end] + numbers[start]>target:
                end -= 1
            else:
                start += 1
        return -1
        
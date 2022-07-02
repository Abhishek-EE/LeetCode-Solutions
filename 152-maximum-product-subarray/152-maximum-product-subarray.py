class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            temp_max = max(max_so_far*curr, min_so_far*curr,curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
            max_so_far = temp_max
            result = max(max_so_far,result)
            
        return result
                            
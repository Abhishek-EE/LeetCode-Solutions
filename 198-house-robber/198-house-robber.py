class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return max(nums)
        n = len(nums)-1
        elem_plus2 = nums[n]
        elem_plus1 = max(nums[n],nums[n-1])
        answer = 0
        for i in range(n-2,-1,-1):
            answer = max(elem_plus1,elem_plus2+nums[i])
            elem_plus2 = elem_plus1
            elem_plus1 = answer
            
        return answer
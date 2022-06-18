class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        You Either include 0 or you don't
        if you don't include zero you want to rob from 1:n and that is the similar as houserobber1
        if you do include zero your answer is zero
        """
        if len(nums) < 4:
            return max(nums)
        return max(nums[0]+self.rob_non_circular(nums[2:len(nums)-1]),self.rob_non_circular(nums[1:]))
    def rob_non_circular(self,nums: List[int])->int:
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
        
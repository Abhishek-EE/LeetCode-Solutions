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
        if len(nums) < 3:
            return max(nums)
        mi2 = 0
        mi1 = nums[len(nums)-1]
        for i in reversed(range(len(nums)-1)):
            mi = max(mi2+nums[i],mi1)
            mi2 = mi1
            mi1 = mi
        return mi
        
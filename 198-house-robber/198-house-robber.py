class Solution:
    def rob(self, nums: List[int]) -> int:
        """The way I feel like we can solve it is you can either rob even houses or odd houses
        see which one has the max, just keep """
        mem = [-1 for i in range(len(nums)+1)]
        if(len(nums)<3):
            return max(nums)
        mi2 = 0
        mi1 = nums[len(nums)-1]
        for i in reversed(range(len(nums)-1)):
            mi = max(mi1,mi2+nums[i])
            mi2 = mi1
            mi1 = mi
        return mi
            
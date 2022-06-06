class Solution:
    def rob(self, nums: List[int]) -> int:
        """The way I feel like we can solve it is you can either rob even houses or odd houses
        see which one has the max, just keep """
        mem = collections.defaultdict(int)
        def robFrom(i):
            if i > len(nums) -2 and i<len(nums)-1:
                mem[i] = nums[i]
                return nums[i]
            if i>len(nums)-1:
                mem[i] = 0
                return 0
            if i in mem:
                return mem[i]
            else:
                answer = max(robFrom(i+1),robFrom(i+2)+nums[i])
                mem[i] = answer
            return answer
        answer = robFrom(0)
        return answer
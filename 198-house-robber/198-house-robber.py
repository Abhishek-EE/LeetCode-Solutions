class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return max(nums)
        mem = collections.defaultdict(int)
        def robFrom(n):
            if n in mem:
                return mem[n]
            if n>len(nums)-1:
                return 0
            if n == len(nums)-1:
                mem[n] = nums[n]
                return mem[n]
            if n == len(nums)-2:
                mem[n] = max(nums[n],nums[n+1])
            ans = max(robFrom(n+1),robFrom(n+2)+nums[n])
            mem[n] = ans
            return mem[n]
        answer = robFrom(0)
            
        return answer
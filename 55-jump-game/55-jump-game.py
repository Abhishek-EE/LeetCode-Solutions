class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        last_success = len(nums) - 1
        for i in reversed(range(n+1)):
            if nums[i] >= last_success - i:
                last_success = i
        if last_success == 0:
            return True
        return False
            

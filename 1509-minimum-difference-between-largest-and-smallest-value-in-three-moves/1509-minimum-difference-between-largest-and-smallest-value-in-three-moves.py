class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        end = len(nums) - 1
        if(end<4):
            return 0
        answer = min(nums[end-3]-nums[start],nums[end-2]-nums[start+1],nums[end-1]-nums[start+2],nums[end]-nums[start+3])
        return answer
        
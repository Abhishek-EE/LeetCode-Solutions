class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = nums[0]
        largestSum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > currentSum+nums[i]:
                currentSum = nums[i]
            else:
                currentSum += nums[i]
            largestSum = max(currentSum,largestSum)
        return largestSum
        
        
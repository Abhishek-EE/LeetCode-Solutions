class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        store = 0
        for i in range(1,len(nums)+1):
            store = store^i
        for i in nums:
            store = store^i
        return store
            
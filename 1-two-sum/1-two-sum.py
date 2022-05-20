class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = collections.defaultdict(int)
        for i in range(len(nums)):
            if target-nums[i] in complement_map:
                return [complement_map[target-nums[i]],i]
            complement_map[nums[i]] = i
        return []
                
        
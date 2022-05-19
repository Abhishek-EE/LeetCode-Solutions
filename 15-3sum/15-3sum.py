class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        complement_map = collections.defaultdict(int)
        twoSumPair = []
        for i in nums:
            if(complement_map[i] != 0):
                add = sorted([i,target-i,-target])
                twoSumPair.append(tuple(add))
            complement_map[target-i] += 1
        return twoSumPair
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        twoSum -> O(n)
        threeSum -> O(n^2)
        '''
        threeSumPair = []
        for i in range(len(nums)-2):
            target = 0 - nums[i]
            threeSumPair.extend(self.twoSum(nums[i+1:],target))
        return list(set(threeSumPair))
            
        
        
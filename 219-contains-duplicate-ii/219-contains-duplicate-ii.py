class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        The most straight forward approach is to first check the
        """
        answer = False
        s = dict()
        for i in range(len(nums)):
            if nums[i] in s:
                answer =  abs(i-s[nums[i]]) <= k or answer
            s[nums[i]] = i
        return answer
        
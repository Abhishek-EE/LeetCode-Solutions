class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        The most straight forward approach is to first check the
        """
        answer = False
        s = dict()
        for i in range(len(nums)):
            if nums[i] in s:
                if abs(i-s[nums[i]]) <= k:
                    answer = True
                    break
            s[nums[i]] = i
        print(s)
        return answer
        
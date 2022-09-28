class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        The easiest solution is create a set 
        and if ever you encounter a repeat return the value then and there
        Otherwise run the entire loop
        """
        s = set(nums)
        if len(s) == len(nums):
            return False
        else:
            return True
        
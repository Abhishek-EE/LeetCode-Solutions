class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        this is same as finding the pivot index
        """
        start = 0
        end = len(nums) - 1
        pivot = 0
        while end-start>=0:
            mid = start + (end-start)//2
            if nums[mid-1] > nums[mid]:
                pivot = mid
                break
            elif nums[mid] < nums[start]:
                end = mid - 1
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                pivot = start
                break
        return nums[pivot]
        
        
        
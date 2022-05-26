class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1
        mid = end - (end - start)//2
        while(end-start>1):
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                end = mid
            else:
                start = mid
            mid = end - (end-start)//2
        if(nums[start] == target):
            return start
        if(nums[mid] == target):
            return mid
        if(nums[end] == target):
            return mid
        
        return -1
        
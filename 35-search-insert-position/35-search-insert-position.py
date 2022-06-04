class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while end-start>=0:
            mid = start + (end-start)//2
            print("start: ",start)
            print("Mid: ", mid)
            print("End: ",end)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        if target> nums[mid]:
            return mid+1
        else:
            return mid
            
        return mid + 1
        
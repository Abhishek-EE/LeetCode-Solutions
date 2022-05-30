class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Find the pivot index -> O(lgn)
        rotate the array around pivot -> O() should be able to do it in constant time
        Find the element in the sorted array -> O(lgn)
        
        '''
        
        start = 0
        end = len(nums) - 1
        pivot_index = 0
        mid = end - (end-start)//2
        while(end>start):
            mid = end - (end - start)//2
            """
            check if mid value is pivot
            """
            if(nums[mid-1] > nums[mid]):
                pivot_index = mid
                break
            """
            if not see if the pivot is in first half or the second half
            """
            if(nums[start]>nums[mid]):
                """
                Pivot is in upper half
                """
                end = mid
                pass
            elif nums[end]<nums[mid]:
                """
                Pivot is in lower half
                """
                start = mid
            else:
                """
                there are not pivot in the array
                """
                break
        print(pivot_index)
        start = 0
        end = len(nums) - 1
        mid = end - (end-start)//2
        while(end-start>1):
            
            print("start: ", (start+pivot_index)%len(nums))
            print("End: ", (end+pivot_index)%len(nums))
            print("Mid: ", (mid+pivot_index)%len(nums))
            if(target == nums[(mid+pivot_index)%len(nums)]):
                return (mid+pivot_index)%len(nums)
            elif target > nums[(mid+pivot_index)%len(nums)]:
                start = mid
            else:
                end = mid
            mid = end - (end-start)//2
        if(nums[(start+pivot_index)%len(nums)] == target):
            return (start+pivot_index)%len(nums)
        if(nums[(end+pivot_index)%len(nums)] == target):
            return (end+pivot_index)%len(nums)
        if nums[(mid+pivot_index)%len(nums)] == target:
            return (mid+pivot_index)%len(nums)
        return -1
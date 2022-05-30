class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        brute force -> traverse the array in O(N) find the location
        O(1)
        Approach is itterative -> additional space is o(1)
        find the pivot in the array using binary search O(lgn)
        one the pivot is found it is very simple to find 
        """
        start = 0
        end = len(nums) - 1
        pivot = 0
        while end-start>=0:
            mid = start + (end-start)//2
            #if the current element is pivot make pivot = mid and break
            if nums[mid-1] > nums[mid]:
                pivot = mid
                break
            #else if the mid element is greater than end element unsorted array is in later half make start = mid + 1
            elif nums[mid] > nums[end]:
                start = mid+1
            #else if the mid elmennt is smaller than the start element unsorted array is in upper half make end = mid - 1
            elif nums[mid] < nums[start]:
                end = mid - 1
            # else the array is perfectly sorted and pivot is basically start of this array
            else:
                pivot = start
                break
        """
        if the target element is greater than pivot index
        need to look from pivot index to end
        if the target elem
        """
        print(pivot)
        start = 0
        end = len(nums) - 1
        if target >= nums[pivot] and target<=nums[end]:
            start = pivot
        else:
            start = 0
            end = pivot - 1
        while end-start>=0:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
        return -1
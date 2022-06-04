# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Binary Search :- 
        """
        start = 0
        end = n
        print(isBadVersion(n))
        while end-start>= 0:
            mid = start + (end-start)//2
            if (isBadVersion(mid) == False) and isBadVersion(mid+1) == True:
                return mid+1
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return 0
        
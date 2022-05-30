# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        """
        Since I know how big the array actually is 
        I can simply use binary search to find the mid valu
        and binary search will give o(lgN) complextiy
        
        """
        start = 0
        end = reader.length() - 1
        while end-start>1:
            mid = start + (end-start)//2
            if (end-start)%2 == 0:
                if(reader.compareSub(start,mid,mid,end)>0):
                    end = mid
                else:
                    start = mid
            else:
                if(reader.compareSub(start,mid,mid+1,end)>0):
                    end = mid
                else:
                    start = mid+1
        if reader.compareSub(start,start,end,end) > 0:
            return start
        else:
            return end
        return 0
        
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        '''
        You could actually do binary search in the 10^4 space which will solve the problem in O(10^4) complexity
        but it will always take that much time which is constant but is almsot always worst case
        '''
        start = 0
        end = pow(10,4)
        while end-start>=0:
            mid = start + (end-start)//2
            print("Start: ", start)
            print("Mid: ",mid)
            print("End", end)
            if(reader.get(mid) == target):
                return mid
            elif reader.get(mid) < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
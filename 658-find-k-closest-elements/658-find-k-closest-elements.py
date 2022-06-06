class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        form a max heap of size k
        traverse the remaining array and if the heap[0][0] > 
        """
        heap = [(-self.abs_diff(x,arr[i]),i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k,len(arr)):
            if heap[0][0] < -self.abs_diff(x,arr[i]):
                print(self.abs_diff(x,arr[i]),i)
                heapq.heappushpop(heap,(-self.abs_diff(x,arr[i]),i))
        return sorted([arr[i[1]] for i in heap])
        
    def abs_diff(self,a,b):
        return abs(b-a)
        
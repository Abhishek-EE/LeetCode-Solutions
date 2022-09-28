class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        
        """
        hash_map = collections.defaultdict(int)
        for i in nums:
            hash_map[i] += 1
        """
        The easiest solution is to sort the hash map by its keys
        and return the sorted keys
        To get a better complexity
        sort the first k elements of the map and then traverse throught the rema
        answer = klgk + n
        """
        return heapq.nlargest(k,hash_map.keys(),key=hash_map.get)
        
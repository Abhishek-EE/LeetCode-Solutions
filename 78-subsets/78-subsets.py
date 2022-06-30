class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Let me see if I can come up with a brute force approach or not
        Find size(0)
        for all the solution of a given size 
        iterate the 
        """
        
        def backtrack(start=0,curr=[]):
            if len(curr) == k:
                answer.append(curr[:])
                return
            for j in range(start,len(nums)):
                curr.append(nums[j])
                backtrack(j+1,curr)
                curr.pop()
        answer = []
        for k in range(len(nums)+1):
            backtrack()
        return answer
                
                
        
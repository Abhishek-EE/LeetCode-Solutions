class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking might be a useful approach
        So this is what I am thinking and correct me If I am wrong
        for i in range(len(nums)):
        backtrack()
        """
        n = len(nums)
        answer = []
        def backtrack(curr=[]):
            if len(curr) == n:
                answer.append(curr)
            for i in nums:
                if i in curr:
                    continue
                else:
                    curr.append(i)
                    backtrack(curr.copy())
                    curr.pop()
        backtrack()
        return answer
                
                
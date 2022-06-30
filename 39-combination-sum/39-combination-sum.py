class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtrack(start=0,curr=[]):
            if sum(curr) == target:
                answer.append(curr[:])
                return
            if sum(curr) > target:
                return
            for i in range(start,len(candidates)):
                curr.append(candidates[i])
                backtrack(i,curr)
                curr.pop()
        backtrack()
        return answer
        
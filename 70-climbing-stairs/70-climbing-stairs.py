class Solution:
    def climbStairs(self, n: int) -> int:
        """
        So how can I reach n steps? 
        climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
        so basically number of ways you can reach n-1 + number of ways you can reach n-2
        """
        if n == 1 or n==2:
            return n
        a1 = 1
        a2 = 2
        for i in range(2,n):
            answer = a1 + a2
            a1 = a2
            a2 = answer
        return answer
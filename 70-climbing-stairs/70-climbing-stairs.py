class Solution:
    def climbStairs(self, n: int) -> int:
        """
        S(n) = S(n-1) + S(n-2)
        """
        if n<=2:
            return n
        m1 = 1
        m2 = 2
        answer = 0
        for i in range(2,n):
            answer = m2 + m1
            m1 = m2
            m2 = answer
        return answer
        
            
        
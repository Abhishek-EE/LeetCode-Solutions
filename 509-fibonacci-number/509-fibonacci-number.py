class Solution:
    def fib(self, n: int) -> int:
        """
        The way to solve a fibonachi problem is
        come up with a recursive solution
        store the answer of subproblem in a hash-map
        reutrn 
        you could do it recursively but let me first do it non recursively
        """
        a0 = 0
        a1 = 1
        answer = n
        for i in range(2,n+1):
            answer = a0 + a1
            a0 = a1
            a1 = answer
        return answer
        
        
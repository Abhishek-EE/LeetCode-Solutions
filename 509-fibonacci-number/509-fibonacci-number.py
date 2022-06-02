class Solution:
    def fib(self, n: int) -> int:
        """
        The way to solve a fibonachi problem is
        come up with a recursive solution
        store the answer of subproblem in a hash-map
        reutrn 
        you could do it recursively but let me first do it non recursively
        """
        A = [0,1]
        for i in range(2,n+1):
            A.append(A[i-1] + A[i-2])
        print(A)
        return A[n]
        
        
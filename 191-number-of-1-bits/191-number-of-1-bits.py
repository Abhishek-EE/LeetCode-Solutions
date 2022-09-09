class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Slowest approach which is like a brute force I guess
        n%2 = 
        n/2
        """
        answer = 0 
        while(n != 0):
            answer += n%2
            n = n//2
        return answer
            
        
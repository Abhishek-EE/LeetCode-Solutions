class Solution:
    def reverseBits(self, n: int) -> int:
        p = 31
        answer = 0
        while n != 0:
            answer += pow(2,p)*(n%2)
            n = n//2
            p -= 1        
        return answer
            
            
            
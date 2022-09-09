class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        There is actually a patter which can be used here
        everytime in a 32 bit number you increase the number by 1 
        0000
        0001
        0011 ->
        0100 -> 4
        0101
        0110
        0111
        
        """
        answer = []
        for i in range(n+1):
            answer.append(self.countOnes(i))
        return answer
            
        
        return answer
    def countOnes(self,n: int)->int:
        answer = 0
        while(n != 0):
            answer += n%2
            n = n//2
        return answer
            
        
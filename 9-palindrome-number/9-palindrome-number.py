class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        start = 0
        end = len(s) - 1
        print(end)
        print(start)
        while(end>=start):
            if(s[end]!=s[start]):
                return False
            end -= 1
            start += 1
        
        return True
    
        
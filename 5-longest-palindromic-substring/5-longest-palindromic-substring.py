class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        """
        s_i = 0
        e_j = 0
        for i in range(len(s)):
            for j in range(i,i+2):
                if j > len(s) - 1:
                    continue
                curr_i,curr_j = self.expandAroundCenter(i,j,s)
                if curr_j - curr_i + 1 > e_j - s_i + 1:
                    s_i = curr_i
                    e_j = curr_j
        return s[s_i:e_j+1]
    
    def expandAroundCenter(self,i,j,s):
        ans_i = i
        ans_j = i
        while i>=0 and j<len(s):
            if s[i] == s[j]:
                ans_i = i
                ans_j = j
            else:
                break
            i -= 1
            j += 1
        
        return (ans_i,ans_j)
                
                
                
                
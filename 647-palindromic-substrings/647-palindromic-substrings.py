class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Ok so if we want to check the number of palindromic substrings
        first thing we need to check 
        Answer[i,j] = Answer[i-1,j+1] + 1*(S[i] == S[j])-> Not really
        is that there are 2n-1 centers which can be used for finding the substring which is palindromic
        so worse case there are going to be n substrings
        now at around each center we could expand around and ever
        abcdabch
        """
        ans = 0
        for i in range(len(s)):
            for j in range(i,i+2):
                if j > len(s)-1:
                    continue
                ans += self.expandAroundCenter(i,j,s)
        return ans
                
                
    def expandAroundCenter(self,i,j,s):
        ans = 0
        while i>=0 and j<len(s):
            if s[i] == s[j]:
                ans += 1
            else:
                break
            i -= 1
            j += 1
        return ans
        
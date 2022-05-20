class Solution:
    def findMaxOccurenceofLetter(self, s: str, letter: chr, k: int)-> int:
        i = 0
        j = 0
        longest_len = 0
        replacement_char = None
        oper_limit = k
        while j < len(s):
            if(s[j]!=letter):
                if(oper_limit != 0):
                    oper_limit -= 1
                else:
                    longest_len = max(longest_len,j-i)
                    if(s[i]!=letter):
                        oper_limit += 1
                    if(j == i):
                        j += 1
                    i += 1
                    continue
            j += 1
        longest_len = max(longest_len,j-i)
        return longest_len
                        
            
    def characterReplacement(self, s: str, k: int) -> int:
        
        s_set = set(s)
        print(k)
        longest_len = 0
        for ch in s_set:
            longest_len = max(longest_len, self.findMaxOccurenceofLetter(s,ch,k))
        return longest_len
            
            
    
                
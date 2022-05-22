class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_idx = 0
        n_idx = 0
        
        while(h_idx <= len(haystack)-len(needle)):
            if(needle == haystack[h_idx:h_idx+len(needle)]):
                return h_idx
                
            h_idx += 1
        return -1
        
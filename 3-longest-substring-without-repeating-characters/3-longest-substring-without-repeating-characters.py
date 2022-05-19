class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        '''
        fast_pointer = 0
        slow_pointer = 0
        lookup = collections.defaultdict(str);
        longest_substring_len = 0
        current_substring_len = 0
        while fast_pointer < len(s):
            print("slow_pointer: ",slow_pointer)
            print("fast_pointer: ",fast_pointer)
            print("longest_susbstring_len: ", longest_substring_len)
            if s[fast_pointer] in lookup and lookup[s[fast_pointer]]>=slow_pointer:
                longest_substring_len = max(longest_substring_len,fast_pointer-slow_pointer)
                slow_pointer = lookup[s[fast_pointer]] + 1
                lookup[s[fast_pointer]] = fast_pointer
                
            else:
                lookup[s[fast_pointer]] = fast_pointer
            fast_pointer += 1
        print("slow_pointer", slow_pointer)
        print("fast_pointer", fast_pointer) 
        longest_substring_len = max(longest_substring_len,fast_pointer-slow_pointer)
        print("longest_substring_len", longest_substring_len)
        return longest_substring_len
            
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Approach ->
        just sort both the letters and compare them 
        if they are equal then they can be anagrams 
        if not they can't be anagrams -> O(nlgn)
        if I use dictionary I could definitely improve on this
        
        """
        s = sorted(s)
        t = sorted(t)
        return s == t
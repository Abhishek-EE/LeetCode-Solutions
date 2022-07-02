class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Iterative answer(s) = 
        """
        mem = collections.defaultdict(int)
        def wordbreak(str1:str):
            ans = False
            if str1 in mem:
                return mem[str1]
            for word in wordDict:
                if len(word)>len(str1):
                    continue
                if str1 == word:
                    return True
                if str1[0:len(word)] == word:
                    ans = ans or wordbreak(str1[len(word):])
            mem[str1] = ans
            return ans
        q = wordbreak(s)
        print(mem)
        return q

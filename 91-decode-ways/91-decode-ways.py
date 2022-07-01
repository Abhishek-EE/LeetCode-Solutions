class Solution:
    def numDecodings(self, s: str) -> int:
        mem = collections.defaultdict(int)
        print(s)
        def decoding(str1):
            """
            if the first element is greater
            """
            print(mem)
            if str1 in mem:
                return mem[str1]
            if len(str1) == 0:
                return 1
            if int(str1[0]) == 0:
                return 0
            if len(str1) < 2:
                return 1
            ans = decoding(str1[1:])
            if int(str1[0:2]) <= 26:
                ans += decoding(str1[2:])
            mem[str1] = ans
            return ans
        answer = decoding(s)
        return answer
        
                
            
                
                
        
            
        
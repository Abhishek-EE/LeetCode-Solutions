class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = collections.defaultdict(int)
        def Change(n):
            if n<0:
                return -1
            if n==0:
                mem[n] = 0
                return 0
            if n in mem:
                return mem[n]
            l = []
            for i in coins:
                ans = Change(n-i)
                if ans >= 0:
                    l.append(ans)
            if len(l) == 0:
                mem[n] = -1
                return -1
            mem[n] = min(l) + 1
            return mem[n]
        answer = Change(amount)
        return answer
                
            
        
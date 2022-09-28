class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closers = {"]":"[","}":"{",")":"("}
        for i in s:
            if i in closers:
                if len(stack)==0 or stack[-1] != closers[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
                
        return len(stack) == 0
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(numRows):
            l = [1]*(i+1)
            for j in range(1,i):
                l[j] = answer[i-1][j-1] + answer[i-1][j]
            answer.append(l)
        return answer
                
        
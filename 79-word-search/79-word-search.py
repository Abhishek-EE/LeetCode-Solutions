class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def backtrack(i=0,j=0,curr=''):
            if len(curr) == 0:
                return True
            if i <0 or j<0 or i>m-1 or j>n-1 or board[i][j]!=curr[0]:
                return False
            board[i][j] = '#'
            if backtrack(i+1,j,curr[1:]):
                return True
            if backtrack(i-1,j,curr[1:]):
                return True
            if backtrack(i,j+1,curr[1:]):
                return True
            if backtrack(i,j-1,curr[1:]):
                return True
            board[i][j] = curr[0]
            return False
        for k in range(m):
            for l in range(n):
                if board[k][l] == word[0]:
                    if backtrack(i=k,j=l,curr=word):
                        return True
        return False
            
            
        
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        There are two parts to this 
        1. Finding where we have all the zeros
        #you could just keep note of all the rows which are to be turned to zero
        #Also keep track of all the columns which needs to be turned to zero
        2. Setting the rows and columns to zero corresponding to a particular zero
        """
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in range(len(matrix)):
            for j in col:
                matrix[i][j] = 0
        
        
        
    
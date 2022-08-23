class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        yeah that is rotation in space not in time
        so traverse the 
        """
        #Rotate the solution across the diagonal
        n = len(matrix)
        for i in range(int(n/2)):
            t = matrix[i]
            matrix[i] = matrix[n-i-1]
            matrix[n-i-1] = t
        for i in range(n):
            for j in range(i,n):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
        
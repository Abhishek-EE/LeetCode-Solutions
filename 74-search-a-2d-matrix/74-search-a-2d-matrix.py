class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Essentially what we have is a sorted list
        we want to do binary search in a sorted list
        now how do we do that actually?
        """
        print(len(matrix))
        """
        this is the relationship which I have been able to observe between the numbers
        one_dimension -> when you divide this by len(matrix[0]) the remainder is the y coordinate and the quotient is the x coordinate
        """
        start = 0
        end = len(matrix)*len(matrix[0]) - 1
        row_len = len(matrix[0])
        while end-start>=0:
            mid = start + (end-start)//2
            i = mid//row_len
            j = mid%row_len
            if(matrix[i][j] == target):
                return True
            elif(matrix[i][j] < target):
                start = mid + 1
            else:
                end = mid - 1
        return False
        
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Let us see what is the spiral order traversal
        1. when go right -> col = col+1
        2. When we go down -> row = row + 1
        3. When we go left -> col = col - 1
        4. When we go up -> row = row - 1
        Start by going right
        When hit a boundary 
        if going right go down
        if going down go left
        if going left go up
        When do you stop, when all the points are visited
        """
        visited = set()
        row_num = len(matrix)
        col_num = len(matrix[0])
        row = 0
        col = 0
        answer = []
        trav_hor = 1
        trav_ver = 1
        horizontal = True
        while len(visited)<row_num*col_num:
            answer.append(matrix[row][col])
            visited.add((row,col))
            if horizontal:
                col_n = col+trav_hor
                if (row,col_n) in visited or col_n >= col_num or col_n < 0:
                    horizontal = False
                    trav_hor = -1*trav_hor
                    row = row + trav_ver
                else:
                    col = col_n
            else:
                row_n = row+trav_ver
                if (row_n,col) in visited or row_n >=row_num or row_n < 0:
                    horizontal = True
                    trav_ver = -1*trav_ver
                    col = col + trav_hor
                else:
                    row = row_n
        return answer
                    
            
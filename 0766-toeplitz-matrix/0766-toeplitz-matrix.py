class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def checkDiagonal(matrix, i, j, rows, cols):
            val = matrix[i][j]
            while i < rows and j < cols:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1
            return True

        rows = len(matrix)
        cols = len(matrix[0])
        
        for j in range(cols):
            if not checkDiagonal(matrix, 0, j, rows, cols):
                return False
        for i in range(1, rows):
            if not checkDiagonal(matrix, i, 0, rows, cols):
                return False
        return True
    

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            x, y = i, 0
            val = matrix[x][y]
            while ( x < len(matrix) and y < len(matrix[0]) ):
                if matrix[x][y] != val:
                    return False 
                x+=1
                y+=1
                
        for i in range(len(matrix[0])):
            x, y = i, 0
            val = matrix[y][x]
            while ( x < len(matrix[0]) and y < len(matrix) ):
                if matrix[y][x] != val:
                    return False 
                x+=1 
                y+=1 
        
        return True

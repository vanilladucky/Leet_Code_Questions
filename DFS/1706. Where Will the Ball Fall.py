class Solution:
    def dfs(self, row, col, grid):
        if row == len(grid):
            return col
        
        if grid[row][col] == 1: # Go to the right
            next_col = col+1
            if (next_col != len(grid[0]) and grid[row][col] == grid[row][next_col]):
                return self.dfs(row+1, next_col, grid)
            else:
                return -1
        
        else: # Go to the left
            next_col = col-1
            if (next_col != -1 and grid[row][col] == grid[row][col-1]):
                return self.dfs(row+1, next_col, grid)
            else:
                return -1
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(grid[0])):
            res.append(self.dfs(0,i,grid))
        return res

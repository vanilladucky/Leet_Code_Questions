""" 
Using a set in Python is very efficient and ideal when we wish to check for identical or repeated elements 
in certain conditions (in row, columns or grids in this case)
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        grid_set = collections.defaultdict(set)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val == ".":
                    continue
                if val in row_set[row] or val in col_set[col] or val in grid_set[(row//3, col//3)]:
                    return False
                row_set[row].add(val)
                col_set[col].add(val)
                grid_set[(row//3, col//3)].add(val)
                
        return True

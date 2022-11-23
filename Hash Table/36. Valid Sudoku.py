class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                ele = board[r][c]
                if ele == '.':
                    continue
                if ele in row[r] or ele in col[c] or ele in grid[(r//3,c//3)]:
                    return False
                row[r].add(ele)
                col[c].add(ele)
                grid[(r//3,c//3)].add(ele)
                
        return True 

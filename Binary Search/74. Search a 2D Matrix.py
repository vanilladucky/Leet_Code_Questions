class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)-1
        
        while left <= right:
            mid = (left+right)//2
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                break
            
        row = (left+right)//2
        
        l, r = 0 , len(matrix[0])-1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
            
        return False

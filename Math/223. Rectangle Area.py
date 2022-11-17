class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        totalarea = abs(ay2-ay1)*abs(ax2-ax1) + abs(by2-by1)*abs(bx2-bx1)
        overlaparea = 0
        
        # Find the overlapping section if there is 
        
        x_overlap = min(ax2,bx2) - max(bx1, ax1)
        y_overlap = min(ay2,by2) - max(ay1, by1)
        
        if x_overlap > 0 and y_overlap > 0: # There is an overlap 
            overlaparea = x_overlap * y_overlap 
            
        return totalarea - overlaparea

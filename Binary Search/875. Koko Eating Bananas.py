class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        
        while lo<hi:
            mid = (lo+hi)//2
            hours_spent = 0
            
            for pile in piles:
                hours_spent += math.ceil(pile/mid)
            
            if hours_spent <= h:
                hi = mid
            else:
                lo = mid + 1
        
        return lo

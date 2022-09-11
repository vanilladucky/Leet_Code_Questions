class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        candidates = zip(speed, efficiency)
        candidates = sorted(candidates, key = lambda x: x[1], reverse=True)
        
        speed = []
        speedsum, res = 0, 0
        
        for s, e in candidates: # The efficiency would always be the minimum
            heapq.heappush(speed, s)
            speedsum += s 
            if len(speed) > k:
                speedsum -= heapq.heappop(speed)
            res = max(res, speedsum*e)
            
        return res % (10 ** 9 + 7)
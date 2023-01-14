class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [i*-1 for i in stones]
        heapq.heapify(stones) # Max Heap 
        
        while len(stones) > 1:
            y, x = heapq.heappop(stones), heapq.heappop(stones)
            if x == y:
                continue
            else:
                remainder = (y-x)
                heapq.heappush(stones,remainder)

        stones.append(0)
        return abs(stones[0])

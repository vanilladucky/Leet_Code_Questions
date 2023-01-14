class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tmp = []
        for point in points:
            x, y = point[0], point[1]
            dist = math.sqrt((x**2) + (y**2))
            tmp.append([dist, [x, y]])

        res = []
        heapq.heapify(tmp)
        for i in range(k):
            ele = heapq.heappop(tmp)
            res.append(ele[1])
        
        return res

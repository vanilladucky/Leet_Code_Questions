class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0 
        q = deque()
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt != 0:
                    q.append([cnt, time+n])
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time 

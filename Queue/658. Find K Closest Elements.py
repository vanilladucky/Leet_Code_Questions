class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = deque()
        
        for i in range(k):
            q.append(arr[i])
            
        for i in range(k, len(arr)):
          
            if abs(x-arr[i]) < abs(x-q[0]) and len(q) == k:
                q.popleft()
                q.append(arr[i])
                
            elif abs(x-arr[i]) > abs(x-q[0]):
                return q
            
        return q

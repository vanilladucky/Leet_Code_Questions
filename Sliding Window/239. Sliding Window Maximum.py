class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        left = 0 
        
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
                
            q.append(r)
            
            if left > q[0]: # Out of range
                q.popleft()
                
            if r+1 >= k:
                res.append(nums[q[0]])
                left+=1
                
        return res

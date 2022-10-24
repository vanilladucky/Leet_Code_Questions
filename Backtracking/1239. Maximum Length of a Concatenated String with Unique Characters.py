class Solution:
    res = 0 
    
    def backtrack(self, arr, idx, local):
        if len(local) != len(set(local)):
            return
            
        self.res = max(self.res, len(local))
        
        for i in range(idx, len(arr)):
            self.backtrack(arr, i+1, local+arr[i])
    
    def maxLength(self, arr: List[str]) -> int:
        # Using BackTracking
        self.backtrack(arr, 0, "")
        return self.res

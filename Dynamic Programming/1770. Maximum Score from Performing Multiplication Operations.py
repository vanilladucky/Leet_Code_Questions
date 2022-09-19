# Dynamic Programming problem and would need to use memoization as we would be attempting to
# obtain maximum of two options - obtaining from left & right

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        memo = {}
        m = len(multipliers)
        n = len(nums)
        
        def dp(i, left):
            if i == m: # End of looping from 0 to m-1
                return 0
            
            if (i,left) in memo:
                return memo[(i,left)]
            
            l = nums[left] * multipliers[i] + dp(i+1, left+1)
            r = nums[(n-1)-(i-left)] * multipliers[i] + dp(i+1, left)
            
            memo[(i,left)] = max(l,r)
            
            return memo[(i,left)]
        
        return dp(0,0)

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        
        def dp(itr, summ):
            
            if (itr, summ) in memo:
                return memo[(itr,summ)]
            
            if summ == target and itr == n:
                return 1 
            
            if (summ == target) or itr >= n:
                return 0
            
            ans = 0
            
            for i in range(1,k+1):
                if target >= i:
                    ans += dp(itr+1, summ+i)
                
            memo[(itr,summ)] = ans
            return ans
                
        return dp(0,0) % (7 + 10**9)

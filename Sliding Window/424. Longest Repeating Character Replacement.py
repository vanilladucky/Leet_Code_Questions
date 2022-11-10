class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        left = 0 
        maxf = 0
        res = 0 
        
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            
            if (r-left+1) - maxf > k:
                count[s[left]] -= 1
                left += 1
                
            res = max(res, r-left+1)
            
        return res

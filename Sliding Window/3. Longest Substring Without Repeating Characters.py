class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeat = set()
        res = 0
        l = 0
        
        for i in range(len(s)):
            while s[i] in repeat:
                repeat.remove(s[l])
                l += 1 # Sliding window technique
            repeat.add(s[i])
            res = max(res, i-l+1)
            
        return res

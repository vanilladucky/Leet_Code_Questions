class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        
        for i in nums:
            if i-1 in hashset:
                continue
            curr = i
            streak = 0
            while curr in hashset:
                streak+=1
                curr+=1
            res = max(res,streak)
            
        return res

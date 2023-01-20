class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subseq = []

        def backtrack(idx):
            if idx == len(nums):
                if len(subseq) >= 2:
                    res.add(subseq)
            if not subseq or subseq[-1] <= nums[idx]:
                subseq.append(nums[idx])
                backtrack(idx+1)
                subseq.pop()
            backtrack(idx+1)
        
        backtrack(0)
        return res

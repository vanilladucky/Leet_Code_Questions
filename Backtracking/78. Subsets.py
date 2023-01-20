# The most basic Backtracking question there is and one everyone learning backtracking should start on.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        res.add(tuple([]))
        tmp = []
        
        def backtrack(idx):
            if idx == len(nums):
                res.add(tuple(tmp))
                return 
            tmp.append(nums[idx])
            backtrack(idx+1)
            tmp.pop()
            backtrack(idx+1)

        backtrack(0)
        return res

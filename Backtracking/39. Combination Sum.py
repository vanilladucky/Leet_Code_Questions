class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, curr, total):
            if total == target:
                res.append(curr.copy())
                return 
            if idx >= len(candidates) or total > target:
                return 

            curr.append(candidates[idx])
            backtrack(idx, curr, total+candidates[idx])
            curr.pop()
            backtrack(idx+1, curr, total)

        backtrack(0, [], 0)
        return res

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, j = 0, 0
        res = 0
        
        while i < len(neededTime) and j < len(neededTime):
            curr_total, curr_max = 0, 0
            
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1
                
            res += (curr_total - curr_max)
            i = j
            
        return res

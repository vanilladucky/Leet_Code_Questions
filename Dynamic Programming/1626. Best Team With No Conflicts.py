class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        zipped = zip(scores, ages)
        zipped = sorted(zipped) # Sorted by score - ascending order

        res = [0] * (max(ages)+1) # Max element would be the answer 

        for score, age in zipped:
            res[age] = score + max(res[:age+1])

        return max(res)

# The hardest DP question I saw so far 

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        dp = [defaultdict(int) for _ in range(len(nums))]  
        n = 0
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                n += dp[j][diff]
                dp[i][diff] += dp[j][diff] + 1 

        return n

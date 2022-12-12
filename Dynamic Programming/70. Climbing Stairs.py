class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        memo = [0]*n
        memo[0], memo[1] = 1, 2

        for i in range(2, n):
            memo[i] = memo[i-2]+memo[i-1]

        return memo[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def solve(x):
            if x > n:
                return 0
            if x == n:
                return 1
            if x in dp:
                return dp[x]
            dp[x] = solve(x+1) + solve(x+2)
            return dp[x]

        return solve(0)
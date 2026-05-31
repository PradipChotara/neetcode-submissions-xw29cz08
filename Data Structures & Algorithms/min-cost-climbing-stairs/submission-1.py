class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n

        def solve(i):

            if i == 0:
                dp[0] = cost[0]
                return dp[0]
            
            if i == 1:
                dp[1] = cost[1]
                return dp[1]

            if dp[i] != -1:
                return dp[i]

            dp[i] = cost[i] + min(solve(i-1), solve(i-2))

            return dp[i]

        solve(n-1),solve(n-2)

        return min(dp[n-1],dp[n-2])
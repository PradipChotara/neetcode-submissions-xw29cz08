class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp[i] -> shows current best from [0 ... i]
        # top down approach (calculate top first in recursion tree using recursion and memoization)

        n = len(nums)
        dp = [-1] * n

        def solve(i):
            # no house left
            if i < 0:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(nums[i]+solve(i-2), solve(i-1))

            return dp[i]

        return solve(n-1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [-1] * n
        
        def solve(i):

            if i < 0:
                return 0

            if i == 0:
                return nums[i]

            if dp[i] != -1:
                return dp[i]

            dp[i] = max(nums[i]+solve(i-2), solve(i-1))

            return dp[i]

        return solve(n-1)
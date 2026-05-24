class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp[i] -> shows current best from [0 ... i]
        # bottom up apprach

        n = len(nums)
        dp = [0] * n

        if n == 1:
            return nums[0]
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]
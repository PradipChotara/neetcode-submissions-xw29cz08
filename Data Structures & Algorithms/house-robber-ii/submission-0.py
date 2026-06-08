class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def dp(arr):
            m = len(arr)
            dp = [-1] * (m+1)

            # solve(i) -> represents max loot till i'th house
            def solve(i):

                if i < 0:
                    return 0
                
                if i == 0:
                    dp[0] = arr[0]
                    return arr[0]

                if dp[i] != -1:
                    return dp[i]

                dp[i] = max(
                    arr[i] + solve(i-2),
                    solve(i-1)
                )

                return dp[i]
            
            solve(m-1)
            return dp[m-1]
        
        return max(
            dp(nums[:-1]),   # include 0th, exclude last
            dp(nums[1:]),    # include last, exclude 1st
        )
        
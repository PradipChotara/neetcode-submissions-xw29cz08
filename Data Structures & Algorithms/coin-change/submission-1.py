class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def solve(amount):

            if amount < 0:
                return float('inf')

            if amount == 0:
                return 0

            if amount in dp:
                return dp[amount]

            ans = float('inf')

            for coin in coins:
                ans = min(ans, 1 + solve(amount-coin))

            dp[amount] = ans
            return ans

        res = solve(amount)

        return -1 if res == float('inf') else res
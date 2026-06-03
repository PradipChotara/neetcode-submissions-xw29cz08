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
                
            res = float('inf')

            for coin in coins:
                res = min(res, 1 + solve(amount - coin))

            dp[amount] = res
            return res

        ans = solve(amount)
        if ans == float('inf'):
            return -1
        else:
            return ans
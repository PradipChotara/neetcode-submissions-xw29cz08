class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def solve(i,curr):

            if i == n:
                if curr == target:
                    return 1
                return 0 

            if (i,curr) in dp:
                return dp[(i,curr)]

            pos = solve(i+1, curr+nums[i])

            neg = solve(i+1, curr-nums[i])

            dp[(i,curr)] = pos + neg

            return dp[(i,curr)]

        return solve(0,0)
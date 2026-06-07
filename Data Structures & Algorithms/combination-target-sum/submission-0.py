class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def solve(index, curr):

            if curr > target:
                return

            if curr == target:
                res.append(subset.copy())
                return
            
            if index == len(nums):
                return

            subset.append(nums[index])
            solve(index, curr + nums[index])

            subset.pop()

            solve(index+1, curr)

        solve(0,0)
        return res
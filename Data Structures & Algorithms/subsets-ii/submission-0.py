class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        nums.sort()

        def solve(index):

            if index == len(nums):
                res.append(subset.copy())
                return

            # take it
            subset.append(nums[index])
            solve(index+1)

            subset.pop()

            # skip it till all duplicates are skipped
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1

            # skip it
            solve(index+1)


        solve(0)
        return res
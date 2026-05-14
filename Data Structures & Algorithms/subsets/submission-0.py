class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(index):
            if index == len(nums):
                res.append(subset.copy())
                return
            
            # choice - take
            subset.append(nums[index])
            dfs(index + 1)

            # undo
            subset.pop()

            # choice - skip
            dfs(index + 1)


        dfs(0)
        return res
        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        candidates.sort()

        def solve(index, curr):

            if curr == target:
                res.append(subset.copy())
                return
            
            if curr > target:
                return

            if index == len(candidates):
                return

            # take it
            subset.append(candidates[index])
            solve(index+1,curr+candidates[index])
            
            subset.pop()

            # skip all duplicates
            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            
            # skip it
            solve(index+1,curr)

        solve(0,0)
        return res
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i in nums:
            if i in hmap:
                return True
            else:
                hmap[i] = 0      
        return False
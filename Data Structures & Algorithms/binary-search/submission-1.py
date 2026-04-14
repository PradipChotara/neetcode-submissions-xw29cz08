class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = ((j-i)//2)+i
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        
        return -1
        
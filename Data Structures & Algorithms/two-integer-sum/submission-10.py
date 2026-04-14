class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            is_there = target - nums[i]
            if is_there in dic and i != dic[is_there]:
                return [i, dic[is_there]]
        return 
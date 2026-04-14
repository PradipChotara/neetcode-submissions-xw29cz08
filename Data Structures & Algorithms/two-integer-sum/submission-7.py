class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        res = []
        for index, value in enumerate(nums):
            # dic[value] = index
            find = target - value
            if find in dic:
                if dic[find] not in res:
                    res.append(dic[find])
                res.append(index)
            dic[value] = index
        return res
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        max_key = nums[0]
        max_val = dic[max_key]

        for key,value in dic.items():
            if value > max_val:
                max_val = value
                max_key = key
            else:
                continue
        return max_key
        
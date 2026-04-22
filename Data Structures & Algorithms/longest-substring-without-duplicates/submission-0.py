class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set = set()
        left = 0 
        right = 0
        max_len = 0

        while right < len(s):
            if s[right] not in c_set:
                c_set.add(s[right])
                right += 1
            else:
                while s[right] in c_set:
                    c_set.remove(s[left])
                    left += 1
                c_set.add(s[right])
                right += 1
            max_len = max(max_len, right-left)
        
        return max_len
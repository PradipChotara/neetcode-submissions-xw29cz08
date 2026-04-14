class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic1 = {}
        dic2 = {}

        for ch in s:
            if ch in dic1:
                dic1[ch] += 1
            else:
                dic1[ch] = 1
        for ch in t:
            if ch in dic2:
                dic2[ch] += 1
            else:
                dic2[ch] = 1
        
        if dic1 == dic2:
            return True
        else:
            return False
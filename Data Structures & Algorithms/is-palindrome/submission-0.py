class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        
        l = 0
        r = len(s)-1

        while l < r:
            # skip alpha Numberic
            if not self.isalphaNum(s[l]):
                l += 1
                continue
            if not self.isalphaNum(s[r]):
                r -= 1
                continue
            # compare
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True    

    def isalphaNum(self, c):
        if 'a' <= c.lower() <= 'z' or '0' <= c <= '9':
            return True
        else:
            return False
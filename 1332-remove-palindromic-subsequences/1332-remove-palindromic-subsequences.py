class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPal(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        if not s:
            return 0
        elif isPal(s, 0, len(s) - 1):
            return 1
        else:
            return 2

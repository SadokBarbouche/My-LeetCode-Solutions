class Solution:
    def palindrome(self, s):
        n = len(s)
        l , r = 0 , n - 1
        for i in range(n // 2):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if self.palindrome(s[i:j+1]):
                    ans += 1
        return ans
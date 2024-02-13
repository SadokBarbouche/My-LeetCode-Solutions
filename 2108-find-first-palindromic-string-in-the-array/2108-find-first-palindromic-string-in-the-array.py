class Solution:
    def pal(self, s):
        l,r = 0,len(s)-1
        while l<=r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.pal(word):
                return word
        return ""
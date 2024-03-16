class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s.lower()))
        for i in range(len(s)//2):
            if s[i] != s[-1 - i] :
                return False
        return True
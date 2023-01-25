class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rep = []
        ans = 0
        length=0
        for i in range(len(s)):
            if s[i] in rep:
                ans = max(ans, length)
                rep = rep[rep.index(s[i])+1:]
                length = len(rep)
            rep.append(s[i])
            length += 1
        ans = max(ans, length)
        return ans
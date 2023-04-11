class Solution:
    def removeStars(self, s: str) -> str:
        l = [c for c in s]
        i = 0
        for c in l:
            if c != "*":
                l[i] = c
                i += 1
            elif i > 0 and l[i-1] != "*":
                i -= 1
        return "".join(l[:i])

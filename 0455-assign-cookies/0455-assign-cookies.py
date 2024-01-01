class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child_i = 0
        for cookie in s:
            if child_i < len(g) and cookie >= g[child_i]:
                child_i += 1
        return child_i

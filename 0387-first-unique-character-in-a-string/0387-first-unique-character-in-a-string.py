class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i, j in enumerate(s):
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
        for i, j in enumerate(s):
            if d[j] == 1:
                return i
        return -1

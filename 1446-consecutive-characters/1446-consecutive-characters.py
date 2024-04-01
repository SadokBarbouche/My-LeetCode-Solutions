class Solution:
    def maxPower(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        length = 1 
        arr = []
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                length += 1
            else:
                arr.append(length)
                length = 1
        arr.append(length)
        return max(arr)

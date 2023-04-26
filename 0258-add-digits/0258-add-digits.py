class Solution:
    def addDigits(self, num: int) -> int:
        size = len(str(num))
        while size > 1:
            ans = sum(int(i) for i in str(num))
            num = ans
            size = len(str(num))
        return num
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = abs(x)//x
        x = abs(x)
        s = [i for i in str(x)][::-1]
        ans = int("".join(s))
        return sign*ans if ans >= -2**31 and ans <= 2**31 - 1 else 0        
        
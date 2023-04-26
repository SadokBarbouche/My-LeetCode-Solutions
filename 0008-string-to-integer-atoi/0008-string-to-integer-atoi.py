class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0 
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        ans = 0
        for c in s:
            if not c.isdigit():
                break
            ans = ans * 10 + int(c)
        
        ans *= sign
        if ans < -2**31:
            return -2**31
        elif ans > 2**31 - 1:
            return 2**31 - 1
        else:
            return ans

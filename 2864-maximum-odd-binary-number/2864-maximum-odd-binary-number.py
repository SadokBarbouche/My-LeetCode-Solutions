class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = {'0': 0, '1': 0} 
        for i in s:
            count[i] += 1
        zeros = count["0"]
        ones = count["1"]
        return "1" * (ones - 1) + "0" * zeros + "1"

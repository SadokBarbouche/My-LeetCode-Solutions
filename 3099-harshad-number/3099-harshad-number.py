class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        harshad = sum([int(i) for i in str(x)])
        return harshad if x % harshad == 0 else -1
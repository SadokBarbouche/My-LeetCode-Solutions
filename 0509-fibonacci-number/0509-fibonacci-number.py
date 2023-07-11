class Solution:
    def fib(self, n: int) -> int:
        assert n >= 0 , "n must be positive"
        if n <= 1 :
            return n
        return self.fib(n-1) + self.fib(n-2)
class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        return int(n**0.5)**2 == n

    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if self.isPerfectSquare(n):
            return 1
        
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (1 if (high - low) % 2 != 0 or low % 2 != 0 else 0)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = 1e9
        for price in prices:
            min_price = min(min_price, price)
            ans = max(ans, price - min_price)
        return ans 
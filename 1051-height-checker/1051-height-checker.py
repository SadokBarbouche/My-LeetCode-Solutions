class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0
        for i in zip(expected,heights):
            ans += i[0] - i[1] != 0
        return ans
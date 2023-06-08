class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in grid[i]:
                if j < 0:
                    ans += 1
        return ans
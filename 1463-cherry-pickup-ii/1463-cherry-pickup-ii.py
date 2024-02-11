class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {}

        def dfs(row, col1, col2):
            if (row, col1, col2) in memo:
                return memo[(row, col1, col2)]

            cherries = grid[row][col1] if col1 == col2 else grid[row][col1] + grid[row][col2]

            if row == rows - 1:
                return cherries

            max_cherries = 0
            for new_col1 in [col1 - 1, col1, col1 + 1]:
                for new_col2 in [col2 - 1, col2, col2 + 1]:
                    if 0 <= new_col1 < cols and 0 <= new_col2 < cols:
                        max_cherries = max(max_cherries, dfs(row + 1, new_col1, new_col2))

            total_cherries = cherries + max_cherries
            memo[(row, col1, col2)] = total_cherries
            return total_cherries

        return dfs(0, 0, cols - 1)
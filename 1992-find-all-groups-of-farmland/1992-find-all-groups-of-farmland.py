class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        result = []
        def dfs(r, c, bottom_right):
            if r < 0 or c < 0 or r >= rows or c >= cols or not land[r][c]:
                return False
            land[r][c] = 0
            bottom_right[0] = max(bottom_right[0], r)
            bottom_right[1] = max(bottom_right[1], c)
            if dfs(r + 1, c, bottom_right) or dfs(r, c + 1, bottom_right) or dfs(r - 1, c, bottom_right) or dfs(r, c - 1, bottom_right):
                return True
            return True
        for r in range(rows):
            for c in range(cols):
                if land[r][c]:
                    bottom_right = [r, c]
                    if dfs(r, c, bottom_right):
                        result.append([r, c] + bottom_right)
        return result
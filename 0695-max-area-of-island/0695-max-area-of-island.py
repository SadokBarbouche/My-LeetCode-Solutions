class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(grid, sr, sc, visited):
            if sr < 0 or sc < 0 or sr >= len(grid) or sc >= len(grid[0]) or (sr, sc) in visited or grid[sr][sc] == 0:
                return 0
            
            visited.add((sr, sc))
            count = 1
            dr = [-1, 0, 1, 0]
            dc = [0, -1, 0, 1]
            for i in range(4):
                count += dfs(grid, sr + dr[i], sc + dc[i], visited)
            
            return count
        
        ans = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    ans = max(ans, dfs(grid, i, j, visited))
            
        return ans

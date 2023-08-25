class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, sr, sc, visited):
            nRows = len(grid)
            nCols = len(grid[0])
            
            if sr < 0 or sc < 0 or sr >= nRows or sc >= nCols or grid[sr][sc] == '0' or (sr, sc) in visited:
                return
            
            visited.add((sr, sc))
            
            dfs(grid, sr + 1, sc, visited)
            dfs(grid, sr - 1, sc, visited)            
            dfs(grid, sr, sc + 1, visited)
            dfs(grid, sr, sc - 1, visited)

            
        nIslands = 0
        visited = set()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(grid, r, c, visited)
                    nIslands += 1
                    
        return nIslands

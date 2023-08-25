class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        def bfs(grid):
            ROWS, COLS = len(grid), len(grid[0])
            if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
                return -1
            
            visit = set()
            queue = deque()
            queue.append((0, 0))
            visit.add((0, 0))

            length = 0
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    if r == ROWS - 1 and c == COLS - 1:
                        return length + 1

                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
                    for dr, dc in neighbors:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 1 or (nr, nc) in visit:
                            continue
                        queue.append((nr, nc))
                        visit.add((nr, nc))
                length += 1
                
            return -1
            
        return bfs(grid)

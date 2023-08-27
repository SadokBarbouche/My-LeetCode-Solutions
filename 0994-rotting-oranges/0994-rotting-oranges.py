class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque()
                    
        # Number of fresh oranges and rotten oranges
        freshOranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i,j))
        if freshOranges == 0:
            return 0
        def timeBfs(grid,freshOranges=freshOranges):
            neighbors = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            time = 0
            while queue:
                print(f'queue = {queue}')
                print(f'visited = {visited}')
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in neighbors:
                        new_r, new_c = r + dr, c + dc
                        
                        if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visited and grid[new_r][new_c] == 1:
                            queue.append((new_r, new_c))
                            visited.add((new_r, new_c))
                            freshOranges -= 1
                            
                time += 1
                

            return time - 1  if freshOranges == 0 else -1
            
        return timeBfs(grid)

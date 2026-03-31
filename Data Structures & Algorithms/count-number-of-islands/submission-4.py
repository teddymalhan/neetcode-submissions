class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = ((0,1), (1,0), (0,-1), (-1,0))

        def checkInBounds(r,c):
            if r >= 0 and r < rows and c >= 0 and c < cols:
                return True

        def dfs(r,c):
            q = deque()
            q.append((r,c))

            while q:
                # basically working as a stack 
                # stack -> dfs
                r, c = q.pop()
                for (dr, dc) in directions:
                    nr, nc = r + dr, c + dc
                    if checkInBounds(nr, nc) and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands +=1
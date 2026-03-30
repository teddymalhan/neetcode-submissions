class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((0,1), (0,-1), (1,0), (-1,0))
        islands = 0

        def inbounds(r, c):
            if r < ROWS and r >= 0 and c >= 0 and c < COLS:
                return True
            return False

        def dfs(r,c):
            # it is inbounds
            if not inbounds(r,c):
                return False
            
            # set to reset
            grid[r][c] = "0"

            # flood fill
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if inbounds(nr,nc) and grid[nr][nc] == "1":
                    dfs(nr,nc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands +=1
                    dfs(r,c)

        return islands
        
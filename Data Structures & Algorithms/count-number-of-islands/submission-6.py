class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((0,1), (0,-1), (1,0), (-1,0))
        if not grid:
            return None
        
        # just a simple flood fill style algo
        def dfs(r, c):
            if not (r >= 0 and r < ROWS and c >= 0 and c < COLS):
                return
            
            if grid[r][c] != "1":
                return

            # set the current spot to be 0
            grid[r][c] = "0"

            # run dfs for all four directions to flood fill them to 0
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                dfs(nr,nc)
            
            return

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def in_bounds(r,c):
            if 0 <= r < rows and 0 <= c < cols:
                return True
            return False

        dirs = ((0,1), (0,-1), (1,0), (-1,0))

        def dfs(r: int, c :int) -> None:
            if not in_bounds(r,c):
                return
            
            # let's visit this node
            grid[r][c] = "0"

            for dr, dc in dirs:
                if in_bounds(r+dr, c+dc) and grid[r+dr][c+dc] == "1":
                    dfs(r+dr, c+dc)

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        
        return islands
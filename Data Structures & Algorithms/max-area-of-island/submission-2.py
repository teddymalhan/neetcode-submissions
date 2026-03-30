class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = ((0,1), (0,-1), (1,0), (-1,0))
        maxArea = 0

        def inbounds(r,c):
            if r < rows and r >= 0 and c < cols and c >= 0:
                return True
            return False

        def dfs(r, c):
            if not inbounds(r,c):
                return 0
            # counting area of the current box
            area = 1
            # visited
            grid[r][c] = 0
            for dr, dc in dirs:
                if inbounds(r+dr, c+dc) and grid[r+dr][c+dc] == 1:
                    area += dfs(r+dr, c+dc)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    maxArea = max(area, maxArea)
        
        return maxArea

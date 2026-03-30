class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        in_bounds = lambda r,c : 0 <= r < rows and 0 <= c < cols
        dirs = ((0,1), (0,-1), (1,0), (-1,0))

        def dfs(r: int, c: int) -> int:
            # print(in_bounds(r,c))
            if not in_bounds(r,c):
                return 0
            
            # mark the current cell as visited
            # by marking it as 2?
            grid[r][c] = 0

            area = 1
            
            for dr, dc in dirs:
                if in_bounds(r+dr, c+dc) and grid[r+dr][c+dc] == 1:
                    area += dfs(r+dr, c+dc)
            return area

        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    maxArea = max(maxArea, area)
        
        return maxArea
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        dirs = ((0,1), (0,-1), (1,0), (-1,0))
        notLandValues = (0, -1)
        # my idea is to go from each treasure chest to all places it can reach
        # do a min of the current value and the value from this chest
        # and do this modification
        def inbounds(r,c):
            if r >= 0 and r < rows and c >= 0 and c < cols:
                return True
            return False

        # we also have to propogate how much distance it is from the treasure chest
        def dfs(r: int, c: int, distance: int):
            if not inbounds(r,c):
                return
            
            if distance > grid[r][c]:
                return
                
            grid[r][c] = min(grid[r][c], distance)

            newdistance = distance + 1
            for dr, dc in dirs:
                if inbounds(r+dr, c+dc) and (grid[r+dr][c+dc] not in notLandValues):
                    dfs(r+dr, c+dc, newdistance)
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dfs(r,c, 0)
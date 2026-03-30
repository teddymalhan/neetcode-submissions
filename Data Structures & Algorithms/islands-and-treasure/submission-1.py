class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        LAND, TREASURE, WATER  = 2147483647, 0, -1
        rows, cols = len(grid), len(grid[0])
        in_bounds = lambda r,c : 0 <= r < rows and 0 <= c < cols
        dirs = ((0,1), (0,-1), (1,0), (-1,0))

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == TREASURE:
                    q.append((r,c, 0))
        
        # we have treasure locations in the queue
        # we do a bfs and search
        # and fill in values
        # as we're starting from the closest treasure to each land we know it will be optimal
    
        # bfs structure bbq -> bfs uses queue
        # pop
        # for nei in node neighboours
        # add neighboours with distance
        # overwrite values if it is lower
        # still need to think about this
        # search for only those which 

        while q:
            r,c, distance = q.popleft()

            if distance:
                grid[r][c] = min(grid[r][c], distance)

            for dr, dc in dirs:
                if in_bounds(r+dr, c+dc) and grid[r+dr][c+dc] == LAND:
                    q.append((r+dr, c+dc, distance + 1))
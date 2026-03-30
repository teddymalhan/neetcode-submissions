class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        rows, cols = len(grid), len(grid[0])
        in_bounds = lambda r, c: 0 <= r < rows and 0 <= c < cols
        dirs = ((0,1), (0,-1), (1,0), (-1,0))

        no_of_fresh_fruits = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == FRESH:
                    no_of_fresh_fruits += 1
                elif grid[r][c] == ROTTEN:
                    q.append((r,c, 0))
            
        
        print(f'no_of_fresh_fruits: {no_of_fresh_fruits}')
        print(f'len(queue): {len(q)}')
        
        counted = 0
        maxTime = 0
        while q:
            r,c, time = q.popleft()
            maxTime = max(time, maxTime)
            for dr, dc in dirs:
                if in_bounds(r+dr, c+dc) and grid[r+dr][c+dc] == FRESH:
                    counted += 1
                    grid[r+dr][c+dc] = ROTTEN
                    q.append((r+dr, c+dc, time + 1))
        
        if no_of_fresh_fruits == counted:
            return maxTime
        else:
            return -1

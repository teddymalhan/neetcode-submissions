class Solution:
    # AIM FOR O(m*n) time and space complexity
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        rows, cols = len(grid), len(grid[0])
        dirs = ((0,1), (0,-1), (1,0), (-1,0))

        def inbounds(r,c):
            if r >= 0 and r < rows and c >= 0 and c < cols:
                return True
            return False

        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == ROTTEN:
                    q.append([r,c,0])
                if grid[r][c] == FRESH:
                    fresh += 1


        max_minute = 0
        while q:
            r, c, minute = q.popleft()
            max_minute = max(max_minute, minute)
            
            # iterate and add all fresh values with one extra minute
            for dr, dc in dirs:
                if inbounds(r+dr, c+dc) and grid[r+dr][c+dc] == FRESH:
                    grid[r+dr][c+dc] = ROTTEN
                    fresh -= 1
                    q.append((r+dr, c+dc, minute + 1))

        return max_minute if fresh == 0 else -1
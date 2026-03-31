class Solution:
    # AIM FOR O(m*n) time and space complexity
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # constants in python
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        rows, cols = len(grid), len(grid[0])
        dirs = ((0,1), (0,-1), (1,0), (-1,0))

        def inbounds(r,c):
            if r >= 0 and r < rows and c >= 0 and c < cols:
                return True
            return False

        def bfs(r: int,c: int, minute: int):
            if not inbounds(r,c):
                return False
            
            grid[r][c] = ROTTEN

            q = deque((r,c, minute))
            while q:
                r, c, minute = q.popleft()
                for dr, dc in dirs:
                    if inbounds(r+dr, c+dc) and grid[r+dr][c+dc] == FRESH:
                        q.append((r+dr, c+dc, minute + 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == ROTTEN:
                    bfs(r,c, 0)

        return -1
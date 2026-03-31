class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        in_bounds = lambda r,c : 0 <= r < rows and 0 <= c < cols
        dirs = ((0,1), (0,-1), (1,0), (-1,0))
        
        # store (r,c) pairs
        pacific = {(0,0), (rows-1, 0), (0, cols-1)}
        # same store (r,c) pairs
        atlantic = {(rows-1,0), (0, cols-1), (rows-1, cols-1)}

        #lets do bfs from the three edges for pacific
        q = deque([(x, 0, heights[x][0]) for x in range(rows)]+[(0, y, heights[0][y]) for y in range(cols)])
        while q:
            r,c, maxHeight = q.popleft() 
            for dr, dc in dirs:
                if (r+dr, c+dc) not in pacific and in_bounds(r+dr, c+dc) and heights[r+dr][c+dc] >= maxHeight:
                    q.append((r+dr, c+dc, heights[r+dr][c+dc]))
                    pacific.add((r+dr, c+dc))

        q = deque([(x, 0, heights[x][0]) for x in range(rows)]+[(rows-1, y, heights[rows-1][y]) for y in range(cols)])
        while q:
            r,c, maxHeight = q.popleft() 
            for dr, dc in dirs:
                if (r+dr, c+dc) not in atlantic and in_bounds(r+dr, c+dc) and heights[r+dr][c+dc] >= maxHeight:
                    q.append((r+dr, c+dc, heights[r+dr][c+dc]))
                    atlantic.add((r+dr, c+dc))
        
        return [[x,y] for x, y in pacific.intersection(atlantic)]
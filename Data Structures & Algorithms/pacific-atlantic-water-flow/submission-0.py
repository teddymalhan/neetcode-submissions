from typing import List, Set, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = ((0,1), (0,-1), (1,0), (-1,0))

        def in_bounds(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r: int, c: int, visited: Set[Tuple[int,int]]):
            if (r, c) in visited:
                return
            visited.add((r, c))  # include the edge cell itself
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                # reverse flow: can move inland if next height >= current height
                if in_bounds(nr, nc) and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        pacific, atlantic = set(), set()

        # Pacific edges: top row & left column
        for c in range(COLS):
            dfs(0, c, pacific)
        for r in range(ROWS):
            dfs(r, 0, pacific)

        # Atlantic edges: bottom row & right column
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic)
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic)

        return [list(rc) for rc in pacific & atlantic]

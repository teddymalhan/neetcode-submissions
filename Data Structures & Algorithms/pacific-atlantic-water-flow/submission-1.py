class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = ((0,1), (0,-1), (1,0), (-1,0))
        pacific, atlantic = [], []

        def ib(r,c):
            if r >= 0 and r < rows and c >= 0 and c < cols:
                return True
            return False

        def dfs(r,c,sea):
            if not ib(r,c):
                return False

            
            if sea == "p":
                if (r,c) in pacific:
                    return
                pacific.append((r,c))
            
            if sea == "a":
                if (r,c) in atlantic:
                    return
                atlantic.append((r,c))
            
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if ib(nr, nc) and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,sea)

        # pacific
        # iterate through first row
        for i in range(cols):
            dfs(0, i, "p")
        
        for i in range(rows):
            dfs(i, 0, "p")


        # atlantic
        # iterate through last row
        for i in range(cols):
            dfs(rows-1, i, "a")
        
        # iterate through last column
        for i in range(rows):
            dfs(i, cols-1, "a")

        return [list((r,c)) for (r,c) in pacific if (r,c) in atlantic]

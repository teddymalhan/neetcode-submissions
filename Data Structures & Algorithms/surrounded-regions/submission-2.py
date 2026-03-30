class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dirs = ((0,1), (0,-1), (1,0), (-1,0))

        def capture(r,c):
            if not (r >= 0 and r < rows and c >= 0 and c < cols and board[r][c] == "O"):
                return

            board[r][c] = "T"

            for dr, dc in dirs:
                capture(r+dr, c+dc)

        # capture unsurrounded regions
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and
                    (r in [0, rows - 1] or c in [0, cols - 1]) 
                ):
                    capture(r,c)
        
        # capture surrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # uncapture unsurrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

                    
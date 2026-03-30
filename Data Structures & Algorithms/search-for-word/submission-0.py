class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = ((0,1), (0,-1), (1,0), (-1,0))

        def dfs(cur, r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == "#":
                return False

            cur += board[r][c]

            if cur == word:
                return True

            ch = board[r][c]
            board[r][c] = "#"

            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if dfs(cur, nr, nc):        
                    return True

            board[r][c] = ch              
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs("", r, c):
                    return True
        return False
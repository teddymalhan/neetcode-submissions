class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRS = ((0,1),(0,-1), (1,0),(-1,0))

        def inbounds(r,c):
            if r >= 0 and r < ROWS and c >= 0 and c < COLS and board[r][c] != "#":
                return True
            return False

        def dfs(r,c, wtn):
            if not inbounds(r,c):
                return False
            
            wtn += board[r][c]

            if wtn == word:
                return True
            
            if len(wtn) >= len(word):
                return False
                
            ch = board[r][c]
            # lets set it to be marked for all recursive searches
            board[r][c] = "#"
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if inbounds(nr,nc) and dfs(nr,nc,wtn):
                    return True
            board[r][c] = ch
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r,c, ""):
                    return True
        
        return False
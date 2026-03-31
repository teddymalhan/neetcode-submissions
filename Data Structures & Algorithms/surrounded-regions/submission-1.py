class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def checkAndModify(r: int, c :int):
            # there are four cases
            # top left, top right, bottom left, bottom right
            # if any are true then we set them to be X

            # when r, c is top left
            topleft = (board[r][c] == 'O' and board[r+1][c] == 'O' and board[r][c+1] == 'O' and board[r+1][c+1] == 'O')
            topright = (board[r][c] == 'O' and board[r+1][c] == 'O' and board[r][c-1] == 'O' and board[r+1][c-1] == 'O')
            bottomleft = (board[r][c] == 'O' and board[r-1][c] == 'O' and board[r][c+1] == 'O' and board[r-1][c+1] == 'O')
            bottomright = (board[r][c] == 'O' and board[r-1][c] == 'O' and board[r][c-1] == 'O' and board[r-1][c-1] == 'O')

            if topleft:
                board[r][c] = 'X' 
                board[r+1][c] = 'X' 
                board[r][c+1] = 'X' 
                board[r+1][c+1] = 'X'

            if topright:
                board[r][c] = 'X' 
                board[r+1][c] = 'X' 
                board[r][c-1] = 'X' 
                board[r+1][c-1] = 'X'

            if bottomleft:
                board[r][c] = 'X' 
                board[r-1][c] = 'X' 
                board[r][c+1] = 'X' 
                board[r-1][c+1] = 'X'

            if bottomright:
                board[r][c] = 'X' 
                board[r-1][c] = 'X' 
                board[r][c-1] = 'X' 
                board[r-1][c-1] = 'X'

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == 'O':
                    checkAndModify(r,c)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = ((0,1), (0,-1), (1,0), (-1,0))


        def dfs(word_till_now, no_of_char_left, row, column):
            if not (row >= 0 and row < ROWS and column >= 0 and column < COLS and board[row][column] != "#")  :
                return False

            word_till_now += board[row][column]

            if word_till_now == word:
                return True

            ch = board[row][column]
            board[row][column] = "#"
            for dr, dc in DIRECTIONS:
                nr, nc = row + dr, column + dc
                if dfs(word_till_now, len(word) - len(word_till_now), nr, nc):
                    return True
            board[row][column] = ch
        
            return False

        for r in range(ROWS):
            for c in range(COLS):
                # tiny optimization to minimize the no of times
                # dfs runs
                if board[r][c] == word[0] and dfs("", len(word), r, c):
                    return True
            
        return False
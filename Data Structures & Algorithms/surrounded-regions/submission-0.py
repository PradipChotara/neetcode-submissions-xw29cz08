class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, convert_to):
            # bound check
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            
            if board[r][c] != 'O':
                return
            
            board[r][c] = convert_to

            dfs(r-1, c, 'S')
            dfs(r+1, c, 'S')
            dfs(r, c-1, 'S')
            dfs(r, c+1, 'S')

        for c in range(cols):
            # top border
            if board[0][c] == 'O':
                dfs(0, c, 'S')
            # bottom border
            if board[rows-1][c] == 'O':
                dfs(rows-1, c, 'S')

        for r in range(rows):
            # left border
            if board[r][0] == 'O':
                dfs(r, 0, 'S')
            if board[r][cols-1] == 'O':
                dfs(r, cols-1, 'S')

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'S':
                    board[r][c] = 'O'

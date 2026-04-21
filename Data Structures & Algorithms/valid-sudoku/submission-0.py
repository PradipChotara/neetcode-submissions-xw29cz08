class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        
        for i in range(row):
            ht = {}
            for j in range(col):
                val = board[i][j]
                if val == ".":
                    continue
                if val not in ht:
                    ht[val] = 1
                else:
                    return False
        
        for i in range(col):
            ht = {}
            for j in range(row):
                val = board[j][i]
                if val == ".":
                    continue
                if val not in ht:
                    ht[val] = 1
                else:
                    return False

        for row in range(0,9,3):
            for col in range(0,9,3):
                ht = {}
                for i in range(3):
                    for j in range(3):
                        val = board[row+i][col+j]
                        if val == ".":
                            continue
                        if val not in ht:
                            ht[val] = 1
                        else:
                            return False
        
        return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = {}

        # Check rows
        for i in range(n):
            m = {}
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] in m:
                    return False
                m[board[i][j]] = 1
        
        # Check cols
        for i in range(n):
            m = {}
            for j in range(n):
                if board[j][i] == ".":
                    continue
                if board[j][i] in m:
                    return False
                m[board[j][i]] = 1

        # Check grids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                m = {}
                for x in range(i, i+3, 1):
                    for y in range(j, j+3, 1):
                        if board[x][y] == ".":
                            continue
                        if board[x][y] in m:
                            return False
                        m[board[x][y]] = 1

        return True
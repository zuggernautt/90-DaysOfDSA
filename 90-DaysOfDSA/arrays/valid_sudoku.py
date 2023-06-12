board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
import collections

# rows = set()
# columns = set()
# grid = set()

# row = set(board)
def isValidSudoku(board):
    rows = set()
    columns = set()
    grid = set()


    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]==".":
                continue
            if (
                board[r][c] in rows[r] or
                board[r][c] in columns[c] or
                board[r][c] in grid[(r//3,c//3)]):
                return False
            rows[r].add(board[r][c])
            columns[c].add(board[r][c])
            grid[(r//3,c//3)].add(board[r][c])
    return True
            



print(isValidSudoku(board))

        





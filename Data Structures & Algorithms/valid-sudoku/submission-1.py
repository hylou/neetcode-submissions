class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # bit mask
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c]) - 1
                cur = 1 << val

                # check row, col and square
                if cur & rows[r] or cur & cols[c] or cur & squares[(r//3)*3+(c//3)]:
                    return False
                else:
                    rows[r] |= cur
                    cols[c] |= cur
                    squares[(r//3)*3+(c//3)] |= cur
        return True

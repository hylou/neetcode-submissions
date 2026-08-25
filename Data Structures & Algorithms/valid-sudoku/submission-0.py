class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkDuplicate(nums: List[str]) -> bool:
            num = [item for item in nums if item != '.']
            return len(num) == len(set(num))

        for i in range(9):

            # check row
            if not checkDuplicate([board[i][j] for j in range(9)]):
                return False
            
            # check column
            if not checkDuplicate([board[j][i] for j in range(9)]):
                return False

            # check square
            # row range: (i//3) * 3 to (i//3 + 1) * 3
            # col range: (i%3) * 3 to (i%3 + 1) * 3
            temp = list()
            for row in range((i//3)*3, (i//3+1)*3):
                for col in range((i%3)*3, (i%3+1)*3):
                    temp.append(board[row][col])
            if not checkDuplicate(temp):
                return False
            
        return True
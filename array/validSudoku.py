class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isInValid(r,c):
            for i in range(9):
                if i != r and board[i][c] == board[r][c]:
                    return True
                if i != c and board[r][i] == board[r][c]:
                    return True
                
            regi_r = r//3
            regi_c = c//3
            
            for i in range(3):
                for j in range(3):
                    if regi_r*3+i != r and regi_c*3+j !=c and board[regi_r*3+i][regi_c*3+j] == board[r][c]:
                        return True
            return False

        for r in range(9):
            for c in range(9):
                if board[r][c]!='.' and isInValid(r,c):
                    return False

        return True
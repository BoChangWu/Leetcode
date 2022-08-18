class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        
        def fill(counter, row_top, row_bottom, col_left, col_right):
            if row_top > row_bottom or col_left > col_right:
                return
            

            for col in range(col_left, col_right+1):
                res[row_top][col] = counter
                counter += 1
                

            for row in range(row_top+1, row_bottom+1):
                res[row][col_right] = counter
                counter += 1
                

            for col in reversed(range(col_left, col_right)):
                res[row_bottom][col] = counter
                counter += 1
                
            for row in reversed(range(row_top+1, row_bottom)):
                res[row][col_left] = counter
                counter += 1
                
            fill(counter, row_top+1, row_bottom-1, col_left+1, col_right-1)
                
            
        fill(1, 0, n-1, 0, n-1)
        return res
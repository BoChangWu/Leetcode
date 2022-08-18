class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral =[]
        seen=set()
        def fill(row_top, row_bottom, col_left, col_right):
            
            if row_top > row_bottom or col_left > col_right:
                print('end')
                return
            

            for col in range(col_left, col_right+1):
                if (row_top,col) not in seen:
                    spiral.append(matrix[row_top][col])
                    seen.add((row_top,col))

            for row in range(row_top+1, row_bottom+1):
                if (row,col_right) not in seen:
                    spiral.append(matrix[row][col_right])
                    seen.add((row,col_right))

            for col in reversed(range(col_left, col_right)):
                if (row_bottom,col) not in seen:
                    spiral.append(matrix[row_bottom][col])
                    seen.add((row_bottom,col))

            for row in reversed(range(row_top+1, row_bottom)):
                if (row,col_left) not in seen:
                    spiral.append(matrix[row][col_left])
                    seen.add((row,col_left))
            fill(row_top+1, row_bottom-1, col_left+1, col_right-1)
        fill(0,len(matrix)-1, 0, len(matrix[0])-1)
        return spiral
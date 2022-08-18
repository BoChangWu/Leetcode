class Solution:
    """
    approach: 
    create a matrix of sum where sum[i][j]th element is the sum
    of all the elements from mat[0][0] to mat[i][j]
    """
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        mat_sum = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        result = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        mat_sum[0][0] = mat[0][0]
        for i in range(1, len(mat)):
            mat_sum[i][0] = mat_sum[i-1][0] + mat[i][0]
        for i in range(1, len(mat[0])):
            mat_sum[0][i] = mat_sum[0][i-1] + mat[0][i]
            
        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                mat_sum[i][j] = mat_sum[i-1][j] + mat_sum[i][j-1] + mat[i][j] - mat_sum[i-1][j-1]
                
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # get the matrix for which we need to get the sum
                start_row = max(i - k, 0)
                end_row = min(i + k, len(mat)-1)
                start_col = max(j - k, 0)
                end_col = min(j + k, len(mat[0])-1)
                if start_row-1<0 and start_col-1<0:
                    result[i][j] = mat_sum[end_row][end_col]
                elif start_row-1<0:
                    result[i][j] = mat_sum[end_row][end_col] - mat_sum[end_row][start_col-1]
                elif start_col-1<0:
                    result[i][j] = mat_sum[end_row][end_col] - mat_sum[start_row-1][end_col]
                else:
                    result[i][j] = mat_sum[end_row][end_col] - mat_sum[start_row-1][end_col] - mat_sum[end_row][start_col-1] + mat_sum[start_row-1][start_col-1]
        # print(result)
        return result
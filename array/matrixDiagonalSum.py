class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        s=0
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r+c ==len(mat)-1 or r==c:

                    s+=mat[r][c]

        return s
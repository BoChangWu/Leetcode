class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        self.min =float('inf')
        
        def dfs(r,c,tmp):
            tmp+= matrix[r][c]
            
            if r+1<len(matrix):
                x=y=float('inf')
                if c-1>=0: x=matrix[r+1][c-1]
                if c+1<len(matrix[0]): y= matrix[r+1][c+1]
                z = matrix[r+1][c]
                dfs(r+1,matrix[r+1].index(min(x,y,z)),tmp)
            else:
                if tmp < self.min: 
                    self.min = tmp
                    print(tmp)
        
        dfs(0,matrix[0].index(min(matrix[0])),0)
            
        return self.min(prev_memo)
class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.c=len(matrix[0]);
        self.r=len(matrix);
        self.dp=[[0 for i in range(self.c+1)] for j in range(self.r+1)];
        for i in range(1,self.r+1):
            for j in range(1,self.c+1):
                self.dp[i][j]=self.dp[i][j-1]+self.dp[i-1][j]-self.dp[i-1][j-1]+matrix[i-1][j-1];
        print (self.dp)        
        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1=r1+1
        c1=c1+1
        r2=r2+1
        c2=c2+1
        return self.dp[r2][c2]-self.dp[r1-1][c2]-self.dp[r2][c1-1]+self.dp[r1-1][c1-1];
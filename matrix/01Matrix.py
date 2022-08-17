class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
        #Output: [[0,0,0],[0,1,0],[0,0,0]]
        m = len(mat)
        n = len(mat[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                elif mat[i][j] == 1:
                    mat[i][j] = 'INF'
        while queue:
            i,j = queue.pop(0)
            dist = mat[i][j] + 1
            for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0<=i+a<m and 0<=j+b<n and mat[i+a][j+b] == 'INF':
                    mat[i+a][j+b] = dist
                    queue.append((i+a,j+b))
        return mat
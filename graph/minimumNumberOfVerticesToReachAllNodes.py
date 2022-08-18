class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        vertices = [0]*n
        for (a,b) in edges:
            vertices[b] +=1
        
        s= []
        for i in range(len(vertices)):
            if vertices[i] ==0:
                s.append(i)
        return s
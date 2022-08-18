
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        num_nodes = len(isConnected)
        provinces = 0
        graph = {}
        graph = {node:[] for node in range(num_nodes)}
        visited = [False]*num_nodes
        
        
        for r in range(num_nodes):
            for c in range(num_nodes):
                if isConnected[r][c] == 1 and r!=c:
                    graph[r].append(c)
                    graph[c].append(r)

        
        def traverse(node):
            # stack = []
            q = deque()
            q.append(node)
            while q:
                curr_node = q.popleft()
                visited[curr_node] = True
                neighbs = graph[curr_node]
                for neigh in neighbs:
                    if not visited[neigh]:
                        q.append(neigh)
            return
        
        
        for node in graph:
            if not visited[node]:
                provinces += 1
                visited[node] = True
                traverse(node)

        return provinces
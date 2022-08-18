class Solution:
    res = float('-inf')
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node, cost):
            self.res = max(self.res, cost) 
            for nei in dic[node]:
                dfs(nei, cost+informTime[node])
                
        dic = {i:[] for i in range(n)}
        for i in range(len(manager)):
            if manager[i]!=-1:
                dic[manager[i]].append(i)
        dfs(headID, 0) 
        return self.res
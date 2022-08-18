class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_path = []
        def dfs(cur,path):
            if cur == len(graph)-1:
                # path= path + [cur]
                all_path.append(path)
            else:
                for i in graph[cur]:
                    dfs(i,path+[i])

        dfs(0,[0])

        return all_path
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        # print(root.children)
        def dfs(node,level):
            if node:
                if len(ans)<= level:
                    ans.append([])
                
                ans[level].append(node.val)
                
                if node.children:
                    for i in node.children:
                        dfs(i,level+1)
            else:
                return
        dfs(root,0)
        return ans
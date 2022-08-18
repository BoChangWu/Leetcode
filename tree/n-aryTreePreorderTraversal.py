class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        l=[]
        def dfs(node):
            if node:
                l.append(node.val)
            
                if node.children:
                    for i in node.children:
                        dfs(i)
        
        dfs(root)
        return l
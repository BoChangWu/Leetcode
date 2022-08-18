class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        l = []
        
        def dfs(node):
            if node:

                if node.left:
                    dfs(node.left)
                    
                l.append(node.val)
                
                if node.right:
                    dfs(node.right)
        dfs(root)
        return l
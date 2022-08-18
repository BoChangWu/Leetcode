class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        l = []
        
        def dfs(node):
            if node:

                if node.left:
                    dfs(node.left)
                
                if node.right:
                    dfs(node.right)
                    
                l.append(node.val)
        dfs(root)
        return l
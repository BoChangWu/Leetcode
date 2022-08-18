
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        l = []
        
        def dfs(node):
            if node:
                l.append(node.val)
            
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
        dfs(root)
        return l
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        self.s= 0
        
        def dfs(node,isLeft):
            
            if not node.left and not node.right:
                if isLeft:
                    self.s+=node.val
            else:
                if node.left:
                    dfs(node.left,True)
                if node.right:
                    dfs(node.right,False)
        
        dfs(root,False)
        
        return self.s
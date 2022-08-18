class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        isSym = True
        
        def dfs(right,left):
            print('k')
            if (right==None and left) or (right and left== None):
                isSym = False
            if right and left:
                if right.val != left.val:
                    isSym=False
                     
                dfs(right.left,left.right)    
                dfs(right.right,left.left)
            
        
        if root.right and root.left:    
            dfs(root.right,root.left)
        
        return isSym
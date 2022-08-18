class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root.val ==val:
            return root
        a=None
        b=None
        if root.left:
            a = self.searchBST(root.left,val)
        if root.right:
            b= self.searchBST(root.right,val)
            
        if a:
            return a
        elif b:
            return b
        else:
            return None
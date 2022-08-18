class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True
        
        def height(node):
            if not node:
                return -1
            
            left = height(node.left)
            right = height(node.right)
            
            if abs(left - right) > 1: #check if the diff is more than 1 update balance
                self.balance = False
                
            return 1+ max(left, right)
        
        height(root)
        return self.balance
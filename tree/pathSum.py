class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        sums=[]
        def dfs(root,curr_sum):
            curr_sum+=root.val
            
            if root.right:
                dfs(root.right,curr_sum)
            if root.left:
                dfs(root.left,curr_sum)
            
            if root.right==None and root.left == None:
                sums.append(curr_sum)
            
        
        dfs(root,0)
        
        return targetSum in sums
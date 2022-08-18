class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        head = root 
        
        nums= []
        
        def dfs(node):
            if node:
                nums.append(node.val)
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
        dfs(root)
        if len(nums)>1:
            for n in nums:
                tmp = list(nums)
                tmp.remove(n)
                if k-n in tmp:
                    return True
                
                
        return False
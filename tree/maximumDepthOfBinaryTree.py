class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        level = 1
        depth =[]
        def dfs(node,l):
            
            if node.left:
                dfs(node.left,l+1)
            if node.right:
                dfs(node.right,l+1)
            
            if not (node.left and node.right):
                depth.append(l)
        if root:
            dfs(root,level)
            return max(depth)
        else:
            return 0
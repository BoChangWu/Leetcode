class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level = 1
        l=[]
        
        def dfs(node,level):
            if len(l)<level:
                l.append([])
                
            l[level-1].append(node.val)
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)
        if root:
            print(root.val)
            dfs(root,level)
        return l
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        zig=[]
        level=1
        rev = False
        
        def dfs(node,lv,re):
            
            if lv>len(zig):
                zig.append([])
            
            if re == False:
                zig[lv-1].append(node.val)
                re = True
            else:
                zig[lv-1].insert(0,node.val)
                re= False
            if node.left:    
                dfs(node.left,lv+1,re)
            if node.right:
                dfs(node.right,lv+1,re)
        
        dfs(root,level,rev)
        
        return zig
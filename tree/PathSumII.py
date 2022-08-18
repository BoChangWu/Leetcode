class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        all_path=[]
        target=[]
        
        def dfs(node,path):
            if node:
                path.append(node.val)
            
                if node.left:
                    p=list(path)

                    dfs(node.left,p)
                if node.right:
                    p=list(path)

                    dfs(node.right,p)
                if node.left==None  and node.right==None:

                    all_path.append(path)

     
        dfs(root,[])

        
        for i in range(len(all_path)):

            if sum(all_path[i]) == targetSum:
                target.append(all_path[i])
        
        return target
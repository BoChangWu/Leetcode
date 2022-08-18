class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        self.find = False
        a = []        
        
        while head :
            a.append(head.val)
            head = head.next            
        
        self.s = ','.join([str(x) for x in a])
        self.find = False

        def dfs(root,pre):
            if not root: return 
                        
            tmp = pre + ',' + str(root.val)

            if self.s in tmp:
                self.find = True 
                return 
            
            if not self.find:
                dfs(root.left, tmp)
                dfs(root.right, tmp)
            
        dfs(root, '')
        return self.find
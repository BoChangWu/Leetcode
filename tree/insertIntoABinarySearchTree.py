class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            head = root
        
        
            while head:

                if val >head.val:
                    if head.right:
                        head = head.right
                        continue
                    else:
                        head.right = TreeNode(val)
                        break
                elif val< head.val:
                    if head.left:
                        head = head.left
                        continue
                    else:
                        head.left = TreeNode(val)
                        break
        else:
            return TreeNode(val)
        return root
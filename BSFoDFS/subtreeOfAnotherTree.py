class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s1 = self.helper(root)
        s2 = self.helper(subRoot)
        return s1.find(s2)!=-1

    def helper(self, root: Optional[TreeNode]) -> str:
        if root:
            return "[" + str(root.val) + "]" +"[" +self.helper(root.left) +"]"  +"[" + self.helper(root.right)
        else:
            return "N"
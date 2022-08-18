class Solution(object):
    def invertTree(self, root):
        if root:
            l = root.left
            root.left = root.right
            root.right = l
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.arr = []
        self.root = root
        
        def check(node):
            
            if node:
                check(node.left)
                self.arr.append(node)
                check(node.right)
        
        check(root)
        self.minNode = TreeNode(self.arr[0].val - 1, left=None, right=root)
        self.current = -1
        
        
        

    def next(self) -> int:
        self.current += 1
        return self.arr[self.current].val
        

    def hasNext(self) -> bool:
        if self.current + 1 < len(self.arr):
            return True
        return False
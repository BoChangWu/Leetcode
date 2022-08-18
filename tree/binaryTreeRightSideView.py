class Solution(object):
    def rightSideView(self, root):
        
        # base case
        if not root:
            return None
        
        queue = [root]
        right_side_view = []
        while len(queue):
            
            # append right-side-view
            right_side_view.append(queue[-1].val)
            
            # prepare children nodes
            children = []
            for node in queue:
                if node.left is not None:
                    children.append(node.left)
                if node.right is not None:
                    children.append(node.right)
            
            queue = children
        
        return right_side_view
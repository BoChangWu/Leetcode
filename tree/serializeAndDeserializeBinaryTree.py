class Codec:
    def serialize(self, root):
        ix = {}
        self._serialize(root, ix, 0)
        return str(ix)
    
    def _serialize(self, node, ix, pos):
        if node:
            ix[pos] = node.val
            self._serialize(node.left, ix, 2*pos + 1)
            self._serialize(node.right, ix, 2*pos + 2)
    
    def deserialize(self, data):
        ix = eval(data)
        return self._deserialize(ix, 0)
        
    def _deserialize(self, ix, pos):
        if pos in ix:
            left = self._deserialize(ix, 2*pos + 1)
            right = self._deserialize(ix, 2*pos + 2)
            return TreeNode(ix[pos], left, right)
        return None
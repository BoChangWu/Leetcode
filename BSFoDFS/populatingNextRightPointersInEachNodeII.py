class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while root:
            cur = root
            while cur:
                nxt = cur.next
                if cur.left and cur.right:
                    cur.left.next = cur.right
                if cur.right or cur.left:
                    while nxt:
                        if nxt.left or nxt.right:
                            (cur.right or cur.left).next = nxt.left or nxt.right
                            break
                        nxt = nxt.next
                cur = nxt

            while root and not root.left and not root.right:
                root = root.next
            root = root and (root.left or root.right)
        return head
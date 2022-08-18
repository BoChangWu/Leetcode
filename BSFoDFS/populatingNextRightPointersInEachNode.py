class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        stack.append(root)
        while(len(stack)):
            tmpStack = []
            
            first = stack.pop(0)
            if first is not None:
                tmpStack.append(first.left)
                tmpStack.append(first.right)
                while(len(stack)):
                    tmpNode = stack.pop(0)
                    if tmpNode is not None:
                        tmpStack.append(tmpNode.left)
                        tmpStack.append(tmpNode.right)
                    first.next = tmpNode
                    first = first.next
            
            stack = tmpStack
            
        return root
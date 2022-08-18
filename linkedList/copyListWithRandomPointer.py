class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if not head:
            return None
        
      
        next_nodes_to_copy = [head]
        
        
        copied_map = { head: Node(head.val) }
        
       
        while next_nodes_to_copy:
            node = next_nodes_to_copy.pop(0)
            copied_node = copied_map[node]

            
            if node.next:
                copied_node.next = self.copy_next_node(next_nodes_to_copy, copied_map, node.next)
            if node.random:
                copied_node.random = self.copy_next_node(next_nodes_to_copy, copied_map, node.random)
    
        return copied_map[head]


    def copy_next_node(self, next_nodes_to_copy, copied_map, next_node):
        
        if next_node not in copied_map:
            copied_map[next_node] = Node(next_node.val)
            next_nodes_to_copy.append(next_node)

        return copied_map[next_node]
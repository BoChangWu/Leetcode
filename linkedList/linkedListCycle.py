class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = []
        if head==None:
            return False
        tail = head
        
        while tail.next:
            if tail in seen:
                return True
            seen.append(tail)
            
            tail=tail.next
        return False
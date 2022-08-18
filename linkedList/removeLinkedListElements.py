class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        tail = head
        list2=ListNode(0)
        head2=list2
        while tail:
            if tail.val !=val:
                head2.next = ListNode(tail.val)
                head2=head2.next
            tail = tail.next
        
        return list2.next
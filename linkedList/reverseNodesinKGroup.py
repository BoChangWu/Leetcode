class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, tail):
            dummy = ListNode()
            m = tail.next
            p = head
            while p and p != m:
                r = dummy.next
                dummy.next = p
                p = p.next
                dummy.next.next = r

            return dummy.next, head

        dummy = ListNode()
        dummy.next = head

        start = dummy
        p = dummy.next
        while p:
            # Find tail
            for i in range(k-1):
                if not p.next:
                    return dummy.next

                p = p.next

            # Reverse
            r = p.next
            new_head, new_tail = reverse(start.next, p)
                
            # Reconnect
            start.next = new_head
            new_tail.next = r

            # Renew variables
            start = new_tail
            p = r

        return dummy.next
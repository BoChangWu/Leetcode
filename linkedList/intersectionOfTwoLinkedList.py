class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
               
                runner1 = head
                runner2 = slow

                while runner1 != runner2:
                    runner1 = runner1.next
                    runner2 = runner2.next
               
                return runner1

        return None
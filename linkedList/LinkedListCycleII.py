class Solution:
    # o(n), o(1)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        slow = head
        fast = head
        # look for a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # intersection exists
            if slow == fast:
                # find the entrance to the cycle
                runner1 = head
                runner2 = slow
                # run at same speed
                while runner1 != runner2:
                    runner1 = runner1.next
                    runner2 = runner2.next
                # return runner1 or runner2
                return runner1
        # no cycle
        return None
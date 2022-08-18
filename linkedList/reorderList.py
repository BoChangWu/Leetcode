class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Purpose: reorder a linked list
        # Intuition: (1) find mid point; (2) reverse second half; (3) merge halved list
        # Example: 1->2->3->4 ==> 1->2 3->4 ==> 1->2 4->3 ==> 1->4->2->3
        

        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        
       
        slow.next = None
        prev = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
       
        first = head
        second = prev
        
        while second:
            next1 = first.next
            next2 = second.next
            
            first.next = second
            first = next1
            
            second.next = first
            second = next2
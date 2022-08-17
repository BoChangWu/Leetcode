class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        
        new_head = ListNode(None)
        new = new_head
        
        while curr1 and curr2:
            if curr1.val < curr2.val:
                new.next = ListNode(curr1.val)
                new = new.next
                curr1 = curr1.next
            else:
                new.next = ListNode(curr2.val)
                new = new.next
                curr2 = curr2.next
                
        while curr1:
            new.next = ListNode(curr1.val)
            new = new.next
            curr1 = curr1.next
            
        while curr2:
            new.next = ListNode(curr2.val)
            new = new.next
            curr2 = curr2.next
                
        new_head = new_head.next
        
        return new_head
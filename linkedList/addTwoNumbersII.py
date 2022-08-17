class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(l1):
            itr = l1
            prev = None
            while itr:
                nxt = itr.next
                itr.next = prev
                prev = itr
                itr = nxt
            return prev
        
        newL1 = reverse(l1)
        newL2 = reverse(l2)
        
        fakeHead = prev = ListNode()
        carry = 0
        while newL1 or newL2:
            if newL1:
                carry += newL1.val
                newL1 = newL1.next
            if newL2: 
                carry += newL2.val
                newL2 = newL2.next
            curr = carry % 10
            carry = carry // 10
            newNode = ListNode(curr)
            
            # create the answer
            prev.next = newNode
            prev = prev.next
        if carry:
            prev.next = ListNode(carry)
        ans = reverse(fakeHead.next)
        return ans
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        h= head
        s=''
        while h:
            s+= str(h.val)
            h= h.next
            
        return int(s,2)
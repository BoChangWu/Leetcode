class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:return None
        last,c=head,1
        
        while last.next!=None:
            c+=1
            last=last.next
        
        
        k=k%c
        if k==0:
            return head
        
        root=head
        
        for i in range(c-k-1):
            root=root.next
        
        last.next=head
        head=root.next
        root.next=None
            
        
        return head
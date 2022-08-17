def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        total = num = count = prev  = post=head 

				# 計算總共有多少個node
        k= 1
        while count.next:
            count= count.next
            k+=1
				
				#如果 倒數第N個剛好是第一個 則直接回傳下個node
        if k-n ==0:
            return head.next
        # 找到第n個node
        for i in range(k-n-1):
            prev = num
            num = num.next

        # 先讓第n-1個node指向n+1個node 再回傳
        if num and num.next:
            num.next = num.next.next
            return total
        else:
            return None
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        result_list = ListNode(999) # Temp Node
        result_list_head = result_list
        
        while list1 and list2:
            if list1.val <= list2.val:
                result_list.next = list1
                list1 = list1.next
            else:    
                result_list.next = list2
                list2 = list2.next
                
            result_list = result_list.next    
        
        if list1 is not None:
            result_list.next = list1 
        elif list2 is not None:
            result_list.next = list2  
        
        return result_list_head.next
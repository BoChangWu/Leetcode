class MyLinkedList:

    def __init__(self):
        # Initialize the list
        self.list1=[]
        return None
        

    def get(self, index: int) -> int:
        if(0<=index<=len(self.list1)-1): #check whether the index is present in list or not
            return self.list1[index]   #return element at that index
        else:
            return -1  
        

    def addAtHead(self, val: int) -> None:
        # List concatenation to add the element at the head of the list
        if(self.list1!=[]):
            self.list1=[val]+self.list1 
        else:
            self.list1=[val]
        return self.list1
        

    def addAtTail(self, val: int) -> None:
        # List concatenation to add the element at the tail of the list
        if(self.list1!=[]):
            self.list1=self.list1+[val]
        else:
            self.list1=[val]
        return self.list1
        

    def addAtIndex(self, index: int, val: int) -> None:
        #check whether the index is wihtin the length of list or not
        if(0<=index<=len(self.list1)-1):
            self.list1=self.list1[0:index]+[val]+self.list1[index:]
        # if index is equal to length of array use list concatenation to add the element at end
        elif(index==len(self.list1)):
            self.list1=self.list1+[val]
        return self.list1
        

    def deleteAtIndex(self, index: int) -> None:
         #check whether the index is wihtin the length of list or not
        if(0<=index<=len(self.list1)-1):
            x=self.list1.pop(index)
            return self.list1
        # Return the list as it is
        else:
            return self.list1
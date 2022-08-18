class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)>=3:
            top = arr.index(max(arr))
            index= 0
            if top == len(arr)-1 or top ==0:
                return False
            
            while index < len(arr):
                if index<top and index+1<len(arr):
                    if arr[index]<arr[index+1]:
                        index+=1
                        continue
                    else:
                        return False
                elif index>=top:
                    if index == len(arr)-1:
                        return True
                    if index+1<len(arr) and arr[index]>arr[index+1]:
                        index+=1
                        continue
                    else:
                        return False
                index+=1
                    
        return False
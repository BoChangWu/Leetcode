class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        s= sum(arr)
        
        if len(arr)>=3:
            for i in range(3,len(arr)+1):
                
                if i % 2==1:
                    
                    for j in range(len(arr)):
                        if j+i<=len(arr):

                        
                            s+=sum(arr[j:j+i])
                        
                        
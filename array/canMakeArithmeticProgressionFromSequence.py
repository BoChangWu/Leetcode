class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        
        for i in range(len(arr)):
            if i <=len(arr)-3:
                if arr[i+2]-arr[i+1] !=arr[i+1]-arr[i]:

                    return False
            
        return True
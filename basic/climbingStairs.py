class Solution:
    def climbStairs(self, n: int) -> int:
    
            if n <=3:
                return n 
            
            length = n + 1
            arr = [0] * length
            
            arr[1] = 1
            arr[2] = 2
            
            for i in range(3,length):
                arr[i] = arr[i-1]+ arr[i-2]
                
            return arr[-1]
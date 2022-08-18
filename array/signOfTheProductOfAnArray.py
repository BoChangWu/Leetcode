class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        p=1
        
        for n in nums :
            if n<0:
                p*=-1
            elif n>0:
                p*=1
            elif n==0:
                return 0
            
        return p
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        
        if n >=0:
            count = 0
            
            bstr = '{0:b}'.format(n)
            
            for b in bstr:
                if b =='1':
                    count+=1
            return count
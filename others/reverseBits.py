class Solution:
    def reverseBits(self, n: int) -> int:
        
        bstr = "{0:b}".format(n)
        
        if len(bstr)< 32:
            
            bstr = '0'*(32-len(bstr)) + bstr
                
        
        nustr=''
        
        for b in bstr:
            nustr = b + nustr
            
        return int(nustr,2)
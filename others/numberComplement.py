class Solution:
    def findComplement(self, num: int) -> int:
        
        bstr = "{0:b}".format(num)
        nstr = ''
        for b in bstr:
            if b == '0':
                nstr+='1'
            if b =='1':
                nstr+='0'
                
        return int(nstr,2)
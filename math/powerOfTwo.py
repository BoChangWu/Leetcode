class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        isTrue = False
        if n <=0:
            return False
        
        if n>1:
            if n%2==0:

                isTrue= self.isPowerOfTwo(n/2)
                return isTrue

            else:
                return False
        else:

            isTrue = True
            return isTrue
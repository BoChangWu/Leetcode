class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            pivot = round(left+(right-left)/2)
            
            
            if isBadVersion(pivot):
                right = pivot
                continue
            else:
                left = pivot + 1 
        
        return left
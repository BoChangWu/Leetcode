class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=list(s)
        a.sort()
        b=list(t)
        b.sort()
        
        if a==b:
            return True
        else:
            return False
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        index=0
        if len(s)==1:
            return 0
        else:
            while index< len(s)-1:

                if s[index] not in s[index+1:] and s[index] not in seen:

                    return index
                seen.add(s[index])
                index+=1
                
        if s[-1] not in seen:
            return len(s)-1
        else:
            return -1
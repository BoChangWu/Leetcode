class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) ==1 and ransomNote in magazine:
                return True
        s = list(ransomNote)

        while len(magazine)>0:
            a= magazine[0]

            for i in range(len(s)):

                if a == s[i]:
                    s.pop(i)
                    break

            magazine=magazine[1:]

        if len(s)>0:
            return False
        else:
            return True
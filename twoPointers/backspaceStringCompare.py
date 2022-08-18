class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        index = 0
        s1= ''
        t1 = ''

        while index <len(s) or index < len(t):

            if index < len(s):
                s1 += s[index]
                if s1[-1] == '#':
                    s1= s1[:-2]

            if index < len(t):
                t1 += t[index]
                if t1[-1] == '#':
                    t1 = t1[:-2]

            index+=1
            
        if s1 == t1 :
            return True
        return False
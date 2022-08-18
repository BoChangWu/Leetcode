class Solution:
    def freqAlphabets(self, s):
        alph = 'abcdefghijklmnopqrstuvwxyz'
        o = []
        new_s = s.split("#")
        breaker = False
        for n in range(len(new_s)) :
            if s.count("#") < len(new_s) and n == len(new_s)-1:
                breaker = True
                break
            if len(new_s[n]) <= 2 :
                o.append(alph[int(new_s[n])-1])
            else :
                for n2 in new_s[n][0:len((new_s[n]))-2] :
                    o.append(alph[int(n2)-1])
                o.append(alph[int(new_s[n][len(new_s[n])-2:])-1])
        if breaker :
            for n in new_s[-1] :
                o.append(alph[int(n)-1])
        return "".join(o)
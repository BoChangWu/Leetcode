class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        import collections
        n=len(p)
        dct1=collections.Counter(p)
        dct2=collections.Counter(s[:n])
        res=[]
        if dct1==dct2: res.append(0)
        for i in range(n,len(s)):
            dct2[s[i-n]]-=1
            if dct2[s[i-n]]==0: del dct2[s[i-n]]
            dct2[s[i]]+=1
            if dct1==dct2:
                res.append(i-n+1)
        return res
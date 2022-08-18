class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        l = [i+1 for i in range(n)]

        while len(l)>1:
            s=l[:k]
            l=l[k:]
            s.pop()
            l=l+s
            

        return l[0]
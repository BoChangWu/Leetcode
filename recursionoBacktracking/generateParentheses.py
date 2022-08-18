class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n ==0:
            return []
        if n ==1:
            return ['()']
        from itertools import permutations
        p=[]
        s = '()'*n
        x = [list(i) for i in list(set(permutations(s,n*2)))]
        m =0

        while m< len(x): 

            if x[m][0] == '(' and x[m][-1]== ')':
                ts = ''
                o =0
                k=0
                while k<len(x[m]):
                    ts+=x[m][k]
                    if x[m][k] =='(':
                        o+=1
                    if x[m][k]==')':
                        o-=1
                    k+=1

                if o==0 and len(ts) == n*2:
                    p.append(ts)

            m+=1
        return p
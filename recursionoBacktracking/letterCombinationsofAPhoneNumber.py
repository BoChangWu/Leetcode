class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) ==0:
            return []
        letter= {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        if len(digits)==1:
            return letter[digits]
        def dfs(index,string):

            if len(string) ==len(digits):
                l.append(string)
            if index+1<len(digits):
                k=0
                while k < len(letter[digits[index+1]]):
                    dfs(index+1,string+letter[digits[index+1]][k])
                    k+=1
        l=[]
        n=0

        while n<len(letter[digits[0]]):

            dfs(0,letter[digits[0]][n])
            n +=1
        return l
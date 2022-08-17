class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
     
        
        def dfs(s,index,path,res):
            if index ==len(s):
                res.append(path)
                
            else:
                if s[index].isalpha():
                    dfs(s,index+1,path+s[index].upper(),res)
                    dfs(s,index+1,path+s[index].lower(),res)
                else:
                    dfs(s,index+1,path+s[index],res)
                    
        
        res = []
        dfs(s,0,'',res)
        return res
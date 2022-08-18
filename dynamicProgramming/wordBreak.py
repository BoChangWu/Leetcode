class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.dic = wordDict
        
        @cache
        def dfs(word):
            if len(word) == 0 or word in self.dic:
                return True
            temp = ""
            for i in range(len(word)):
                temp+=word[i]
                if temp in self.dic:
                    if dfs(word[i+1:]): return True
            
            return False
        
        
        return dfs(s)
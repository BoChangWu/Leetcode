class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count=0
        
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                count+=1
                if i-1>0 and not s[i-1].isalpha():
                    break
        
        return count
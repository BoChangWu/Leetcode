class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        s=''
        index1=0
        index2=0
        while index1<len(word1) or index2<len(word2):
            
            if index1<len(word1):
                s+=word1[index1]
                index1+=1
            if index2<len(word2):
                s+=word2[index2]
                index2+=1
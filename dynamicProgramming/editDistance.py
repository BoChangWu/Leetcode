class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1 = len(word1)
        n2 = len(word2)
        
        old = [i for i in range(n2+1)]
        
        for i in range(n1):
            new = [0 for _ in range(n2+1)]
            new[0] = i + 1
            for j in range(1,n2+1):
                if word2[j-1] == word1[i]:
                    new[j] = old[j-1]
                else:
                    new[j] = 1 + min([old[j-1], old[j], new[j-1]])
            old  = new
        return old[-1]
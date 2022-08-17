class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        from itertools import combinations
        

            
        comb = combinations([i+1 for i in range(n)],k)
        
        return comb
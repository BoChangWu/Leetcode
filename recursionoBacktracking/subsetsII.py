class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        n =0
        sub = []
        while n <=len(nums):
            c = combinations(nums,n)
            
            for i in c:
                a = list(i)
                a.sort()
                if a not in sub:
                    sub.append(a)
            
            n+=1
        return sub
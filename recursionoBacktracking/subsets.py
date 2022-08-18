class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        n =0
        sub = []
        while n <=len(nums):
            c = combinations(nums,n)
            
            for i in c:
                sub.append(list(i))
            
            n+=1
        return sub
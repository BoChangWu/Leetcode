class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        p = list(permutations(nums,len(nums)))
        l = []
        for i in p:
            if list(i) not in l:
                l.append(list(i)) 
        return l
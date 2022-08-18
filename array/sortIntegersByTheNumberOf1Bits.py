class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        arr = [bin(x)[2:] for x in arr]
        
        arr = sorted(sorted(arr), key = lambda x: (x.count('1'), len(x)))
        
        return [int(k, 2) for k in arr]
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        def sum(nums):
            l =[]
            for i in range(len(nums)-1):
                l.append(nums[i]+nums[i+1])
            return l

        if rowIndex <2:
            return [1]*(rowIndex+1)
        
        else:
            row= [1,1]
            for i in range(1,rowIndex):
                row = [1]+sum(row)+[1]
            return row
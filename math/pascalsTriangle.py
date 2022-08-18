class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []
        def sum(nums):
            l =[]
            for i in range(len(nums)-1):
                l.append(nums[i]+nums[i+1])
            return l

        if numRows <3:
            for i in range(numRows):
                pascal.append([1]*(i+1))
        else:

            for i in range(numRows):

                if i < 2:
                    pascal.append([1]*(i+1))
                else:
                    pascal.append([1]+sum(pascal[i-1])+[1])
        return pascal
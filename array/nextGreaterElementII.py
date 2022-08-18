class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = []
        
        def chk(i):
            k = (i+1)%n
            while k!=i:
                if nums[k]>nums[i]:
                    ans.append(nums[k])
                    return
                k= (k+1)%n
            ans.append(-1)
        
        for i in range(len(nums)):
            chk(i)
        return ans
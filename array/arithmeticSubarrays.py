class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = [True]*len(l)
        for i in range(len(l)):
            
            if r[i]+1 < len(nums):
                tmp = nums[l[i]:r[i]+1]
            else:
                tmp = nums[l[i]:]
            tmp.sort()
            diff = tmp[1]=tmp[0]
            for i in range(1,len(tmp)):
                if tmp[i]-tmp[i-1] != diff:
                    ans[i] = False
                    break
            
        return ans
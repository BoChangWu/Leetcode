class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length=len(nums)
        maxEndingHere=[1]*length
        count=[1]*length
        for i in range(1,length):
            for j in range(i):
                if nums[j]<nums[i]:
                    if maxEndingHere[i]<=maxEndingHere[j]:
                        maxEndingHere[i]=maxEndingHere[j]+1
                        count[i]=count[j]
                    elif maxEndingHere[i]==maxEndingHere[j]+1:
                        count[i]+=count[j]

        maxValue=max(maxEndingHere)
        result=0
        for i,num in enumerate(maxEndingHere):
            if num==maxValue:
                result+=count[i]
        return result
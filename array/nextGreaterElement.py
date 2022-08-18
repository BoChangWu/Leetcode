class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans=[]
        
        def chk(index,target):
            if nums2[index]>target:
                ans.append(nums2[index])
            else:
                if index+1<len(nums2):
                    chk(index+1,target)
                else:
                    ans.append(-1)
        
        for i in nums1:
            index = nums2.index(i)
            if index+1<len(nums2):
                chk(index+1,i)
            else:
                ans.append(-1)
        
        return ans
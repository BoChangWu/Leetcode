class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums=[]
        if len(nums1)<len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    del nums2[nums2.index(nums1[i])]
                    nums.append(nums1[i])
        else:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    del nums1[nums1.index(nums2[i])]
                    nums.append(nums2[i])
        return nums
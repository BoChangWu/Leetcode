class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 1
        
        pre = nums[1]-nums[0]
        ans = [pre]
        for i in range(2,len(nums)):
            
            n = nums[i]-nums[i-1]
            print(pre,n)
            if n== 0:
                continue
            if pre >0 and n<0:
                ans.append(n)
                pre=n
            elif pre<0 and n>0:
                ans.append(n)
                pre=n
            else:
                
                ans.pop()
                ans.append(n)
                pre=n
                print('pop')
            
        return len(ans)+1
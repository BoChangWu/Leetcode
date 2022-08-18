import collections
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Compute P[j] = sum(B[:j]) for the fixed array B = A+A
        P = [0]
        
        for _ in range(2):
            for x in nums:
                P.append(P[-1]+x)
                
                

        
        ans = nums[0]
        deque = collections.deque([0])
        for j in range(1,len(P)):
           
            if deque[0]<j-N:
                deque.popleft()
          
            ans = max(ans,P[j]-P[deque[0]])
            
         
            while deque and P[j]<=P[deque[-1]]:
                deque.pop()
                
            deque.append(j)
            
        return ans
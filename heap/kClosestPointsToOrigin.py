class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq
        
        heap = []
        
        for x,y in points:
            heapq.heappush(heap,[x**2+y**2,[x,y]])
        
        ans = []
        for i in range(k):
            a= heapq.heappop(heap)
            ans.append(a[1])
        return ans
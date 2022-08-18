class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        import heapq
        c = Counter(s)
        heap = []
        for key, value in c.items():
            heapq.heappush(heap, (-1*value,key))
            
            
        ans = ""
        while heap:
            n = heapq.heappop(heap)
            ans += n[1]*-n[0]
        return ans
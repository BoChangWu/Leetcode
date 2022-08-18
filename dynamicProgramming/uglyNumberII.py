import heapq
class Solution:
    def nthUglyNumber(self, n):
        primes, heap, dp, visited = [2,3,5], [], [1], set()

        for i, prime in enumerate(primes):
            heapq.heappush(heap, (prime, i, 0))

        while len(dp) < n:
            val, prime_idx, dp_idx = heapq.heappop(heap)
            # print(val,prime_idx,dp_idx)
            if val not in visited:
                visited.add(val)
                dp.append(val)

            heapq.heappush(heap, (primes[prime_idx]*dp[dp_idx+1], prime_idx, dp_idx + 1))
            # print(heap)
        return dp[-1]
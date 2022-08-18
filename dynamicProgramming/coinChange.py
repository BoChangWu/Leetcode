class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        Q = [(amount, 0)]
        done = {amount}
        while Q:
            a, count = Q.pop(0)
            for c in coins:
                d = a - c
                if d == 0:
                    return count + 1
                if d < 0:
                    continue
                if d not in done:
                    Q.append((d, count + 1))
                    done.add(d)
                
        return -1
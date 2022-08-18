from collections import deque
from itertools import product
class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        maxi, maxj = len(grid), len(grid[0])
        queue = deque([(0, 0, 1)])

        if grid[0][0] or grid[-maxi][-maxj]: # unreachable
            return -1

        while queue:
            i, j, d = queue.popleft()
            if (i, j) == (maxi-1, maxj-1):
                return d
            for di, dj in product([-1, 0, 1], repeat=2):
                newi, newj = i + di, j + dj
                if 0 <= newi < maxi and 0 <= newj < maxj:
                    if grid[newi][newj] == 0:
                        grid[newi][newj] = 1
                        queue.append((newi, newj, d + 1))
        return -1
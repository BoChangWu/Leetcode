class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count = 0
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]=='1'):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))
        l = list(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))
        for i in l:
            if i !=0:
                count+=1
        return count
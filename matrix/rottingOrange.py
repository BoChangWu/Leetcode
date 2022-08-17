class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # add rotten oranges to a queue and keep track of fresh oranges
        queue = []
        num_fresh = 0
        minute = 0

        # initialize the queue with rotten oranges
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 2:
                    queue.append((m, n))
                elif grid[m][n] == 1:
                    num_fresh += 1

        if num_fresh == 0:
            return 0 # no fresh oranges to begin with
        if len(queue) == 0:
            return -1 # no rotten oranges to begin with

        while queue:
            # BFS == level order traversal (same technique!)
            num_rotten = len(queue)
            minute += 1
            for i in range(num_rotten):
                (m, n) = queue.pop(0) # get the next rotten orange from the queue

                # get four directions in the grid
                left = 0 if n == 0 else n - 1
                right = len(grid[0]) - 1 if n == len(grid[0]) - 1 else n + 1
                up = 0 if m == 0 else m - 1
                down = len(grid) - 1 if m == len(grid) - 1 else m + 1

                # check if the neighbors are rotten
                if grid[m][left] == 1:
                    grid[m][left] = 2
                    num_fresh -= 1
                    queue.append((m, left))
                if grid[m][right] == 1:
                    grid[m][right] = 2
                    num_fresh -= 1
                    queue.append((m, right))
                if grid[up][n] == 1:
                    grid[up][n] = 2
                    num_fresh -= 1
                    queue.append((up, n))
                if grid[down][n] == 1:
                    grid[down][n] = 2
                    num_fresh -= 1
                    queue.append((down, n))

        # if there are fresh oranges remaining, return -1
        if num_fresh > 0:
            return -1

        return minute - 1
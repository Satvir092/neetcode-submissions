class Solution:
    from collections import deque
    def shortestBridge(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        explored = set()

        others = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c):

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in explored:

                return

            explored.add((r, c))

            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)

        def bfs():

            queue = deque(explored)

            output = 0

            while queue:

                for _ in range(len(queue)):

                    r, c = queue.popleft()

                    for dr, dc in others:

                        curR, curC = r + dr, c + dc

                        if curR < 0 or curC < 0 or curR >= rows or curC >= cols or (curR, curC) in explored:

                            continue

                        if grid[curR][curC] == 1:

                            return output

                        explored.add((curR, curC))
                        queue.append((curR, curC))

                output += 1

        for i in range(rows):

            for j in range(cols):

                if grid[i][j] == 1:

                    dfs(i, j)
                    return bfs()


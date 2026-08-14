class Solution:
    from collections import deque

    def orangesRotting(self, grid: List[List[int]]) -> int:

        totals = 0

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))

        while queue:

            rotted = False

            for _ in range(len(queue)):

                r, c = queue.popleft()

                neighbors = [
                    (r + 1, c),
                    (r - 1, c),
                    (r, c + 1),
                    (r, c - 1)
                ]

                for nr, nc in neighbors:

                    if nr < 0 or nc < 0 or nr == rows or nc == cols:
                        continue

                    if grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    rotted = True

            if rotted:
                totals += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return totals
        
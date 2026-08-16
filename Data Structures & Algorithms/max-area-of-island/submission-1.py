class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque

        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        max_area = 0
        cur_area = 0

        for i in range(rows):

            for j in range(cols):

                if grid[i][j] == 1:

                    queue.append((i, j))

        while queue:

            r, c = queue.popleft()

            if (r, c) in visited:

                continue

            inner_queue = deque()

            inner_queue.append((r, c))

            while inner_queue:

                rr, cc = inner_queue.popleft()

                if rr < 0 or cc < 0 or rr >= rows or cc >= cols or grid[rr][cc] == 0 or (rr, cc) in visited:

                    continue

                visited.add((rr, cc))

                cur_area += 1

                inner_queue.append((rr + 1, cc))
                inner_queue.append((rr - 1, cc))
                inner_queue.append((rr, cc + 1))
                inner_queue.append((rr, cc - 1))

            max_area = max(max_area, cur_area)
            cur_area = 0

        return max_area

            





        
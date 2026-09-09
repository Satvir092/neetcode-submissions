class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        seen = set()

        def dfs(r, c):

            if r < 0 or c < 0 or r >= rows or c >= cols:
                return -1000000

            if (r, c) in seen or grid[r][c] == 0:
                return 0

            seen.add((r, c))

            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        output = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1 and (i, j) not in seen:

                    result = dfs(i, j)

                    if result >= 0:
                        output += result

        return output

             

            


        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])


        visit = set()

        def dfs(r, c, index):

            if index == len(word):

                return True

            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or board[r][c] != word[index]:

                return False

            visit.add((r, c))

            res = (dfs(r - 1, c, index + 1) or
            dfs(r + 1, c, index + 1) or
            dfs(r, c + 1, index + 1) or dfs(r, c - 1, index + 1))
            visit.remove((r, c))
            return res

        
        for i in range(rows):

            for j in range(cols):

                if dfs(i, j, 0):

                    return True
                
        return False


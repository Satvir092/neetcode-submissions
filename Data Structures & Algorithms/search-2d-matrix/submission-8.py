class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        i = 0

        while i < rows:

            if target > matrix[i][cols - 1]:

                i += 1 
                continue

            k = 0
            r = cols - 1

            while k <= r:

                mid = (k + r) // 2

                print(matrix[i][mid], mid)

                if matrix[i][mid] == target:

                    return True

                elif target < matrix[i][mid]:

                    r = mid - 1

                else:

                    k = mid + 1

            return False

        return False
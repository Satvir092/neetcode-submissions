class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        from collections import deque

        from collections import defaultdict

        ad_mat = defaultdict(list)

        for left, right in edges:

            ad_mat[left].append(right)
            ad_mat[right].append(left)

        heights = []

        for i in range(n):

            queue = deque([(i, 0)])

            visited = {i}

            height = 0

            while queue:

                root, distance = queue.popleft()

                height = max(height, distance)

                for neighbor in ad_mat[root]:

                    if neighbor not in visited:

                        visited.add(neighbor)

                        queue.append((neighbor, distance + 1))

            heights.append(height)

        mini = min(heights)

        indicies = []

        for i in range(len(heights)):

            if heights[i] == mini:

                indicies.append(i)

        return indicies



        
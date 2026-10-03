class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        from collections import deque
        from collections import defaultdict
        
        output = []
        tree_h = defaultdict(list)

        min_height = 100000000000000

        for left, right in edges:

            tree_h[left].append(right)
            tree_h[right].append(left)


        for i in range(n):

            queue = deque([i])
            visited = set([i])
            
            c_height = 0

            while queue:

                for _ in range(len(queue)):

                    node = queue.popleft()

                    for nei in tree_h[node]:

                        if nei not in visited:

                            visited.add(nei)
                            queue.append(nei)

                c_height += 1

            if c_height == min_height:

                output.append(i)

            elif c_height < min_height:
                
                min_height = min(c_height, min_height)
                output = []
                output.append(i)

        return output







            
        
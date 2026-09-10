class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        from collections import defaultdict

        seen = defaultdict(list)
        cycle = set()
        visited = set()

        for crs, pre in prerequisites:
            seen[crs].append(pre)

        def dfs(crs):

            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)

            for prer in seen[crs]:
                if not dfs(prer):
                    return False

            cycle.remove(crs)
            visited.add(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True

        

        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict

        courses = defaultdict(list)
        output = []
        visited = set()
        cycle = set()

        for crs, pre in prerequisites:
            courses[crs].append(pre)

        def dfs(crs):

            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)

            for pre in courses[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visited.add(crs)

            output.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return output
        
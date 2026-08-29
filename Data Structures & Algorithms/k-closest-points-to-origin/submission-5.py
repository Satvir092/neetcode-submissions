class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math

        heap = []

        output = []

        for point in points:

            distance = math.sqrt(point[0]**2 + point[1]**2)

            heap.append((distance, [point[0], point[1]]))


        heapq.heapify(heap)

        for _ in range(k):

            c_distance, point = heapq.heappop(heap)
            output.append(point)

        return output
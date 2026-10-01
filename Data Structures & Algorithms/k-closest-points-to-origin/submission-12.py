class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        import math

        hash_map = {}

        i = 0

        ar = []

        for x2, y2 in points:

            distance = math.sqrt(((0 - x2)**2 + (0 - y2)**2))

            hash_map[((x2, y2), i)] = distance

            i += 1

        sorted_data = dict(sorted(hash_map.items(), key=lambda item: item[1]))

        print(sorted_data)

        
        for key in sorted_data:

            if k > 0:

                ar.append(key[0])
                k-=1

            else:

                break

        return ar
        
class Solution:
    def customSortString(self, order: str, s: str) -> str:

        order_map = {}

        for i in range(len(order)):
            order_map[order[i]] = i

        s = list(s)

        s.sort(key=lambda x: order_map.get(x, len(order)))

        return "".join(s)



        
class Solution:
    from collections import defaultdict
    def totalFruit(self, fruits: List[int]) -> int:

        maxi = 0
        types = defaultdict(int)
        l = 0
        r = 0
        current = 0

        while r < len(fruits):

            types[fruits[r]] += 1

            current += 1

            while len(types) > 2:

                types[fruits[l]] -= 1

                if not types[fruits[l]]:

                    types.pop(fruits[l])

                l += 1
                
                current -= 1

            r += 1

            maxi = max(maxi, current)


        return maxi

        
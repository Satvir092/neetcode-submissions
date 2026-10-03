class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        from collections import defaultdict

        output = 0

        r = 0
        l = 0
        maxi = 0

        hash_set = defaultdict(int)

        while r < len(fruits):

            print(hash_set, output)


            hash_set[fruits[r]] += 1
            output += 1

            if len(hash_set) > 2:

                while len(hash_set) > 2:

                    hash_set[fruits[l]] -= 1
                    if hash_set[fruits[l]] == 0:

                        del hash_set[fruits[l]]
                    
                    l += 1

                    output -= 1

            r += 1

            maxi = max(output, maxi)

        return maxi




        
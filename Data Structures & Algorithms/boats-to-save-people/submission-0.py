class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        l = 0
        r = len(people) - 1

        visited = []

        output = 0

        while l < r:

            if people[l] + people[r] <= limit:

                output += 1

                l += 1
                r -= 1

            else:

                r -= 1
                output += 1

        if l == r:

            output += 1

        return output
            




        
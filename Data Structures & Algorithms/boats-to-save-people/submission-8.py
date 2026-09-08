class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        output = 0

        l = 0

        r = len(people) - 1

        while l <= r:

            if people[r] + people[l] > limit:

                output += 1

                r -= 1

            else:

                l += 1
                r -= 1

                output += 1

        return output

        
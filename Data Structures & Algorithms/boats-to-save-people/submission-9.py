class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0

        r = len(people) - 1
        c = 0

        while l <= r:

            c_sum = people[l] + people[r]

            if c_sum <= limit:

                c += 1
                l += 1
                r -= 1

            elif c_sum > limit:
                r -= 1
                c += 1

        return c


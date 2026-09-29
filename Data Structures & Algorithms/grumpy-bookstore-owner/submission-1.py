class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        l = 0
        r = 0
        maxi = 0
        current = 0
        base = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                base += customers[i]

        while r < len(customers):

            if grumpy[r] == 1:
                current += customers[r]

            while r - l + 1 > minutes:

                if grumpy[l] == 1:
                    current -= customers[l]

                l += 1

            maxi = max(maxi, current)

            r += 1

        return base + maxi
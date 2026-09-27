class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        from collections import defaultdict

        output = 0

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        for el, cou in counts.items():

            if cou % 3 == 0 and cou >= 3:

                output += cou / 3

            elif (cou - 2) % 3 == 0 and cou >= 2:

                output += (cou - 2) / 3 + 1

            elif (cou - 4) % 3 == 0 and cou >= 4:

                output += (cou - 4) / 3 + 2

            else:

                return -1

        return int(output)


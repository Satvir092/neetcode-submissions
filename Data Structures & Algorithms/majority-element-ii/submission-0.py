class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        from collections import defaultdict

        import math

        hash_map = defaultdict(int)

        output = []

        maxi = math.floor(len(nums)/3)

        for num in nums:

            hash_map[num] += 1

        for key in hash_map:

            if hash_map[key] > maxi:

                output.append(key)

        return output

            




        
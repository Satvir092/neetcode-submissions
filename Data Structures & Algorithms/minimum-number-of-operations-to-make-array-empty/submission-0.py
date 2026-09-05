class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        from collections import defaultdict

        hash_map = defaultdict(int)

        for num in nums:

            hash_map[num] += 1

        res = 0

        for n, c in hash_map.items():

            if c == 1:

                return -1

            res += math.ceil(c / 3)

        return res

                    

        
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        hash_map = {0:1}

        output = 0

        pre_sum = 0

        for num in nums:

            pre_sum += num

            needed = pre_sum - goal

            output += hash_map.get(needed, 0)

            hash_map[pre_sum] = hash_map.get(pre_sum, 0) + 1

        return output
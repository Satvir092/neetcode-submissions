class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dfs(n):

            if n == 0:
                return nums[0]

            if n == 1:
                return max(nums[0], nums[1])

            if n in memo:
                return memo[n]

            memo[n] = max(nums[n] + dfs(n - 2), dfs(n - 1))

            return memo[n]

        return dfs(len(nums) - 1)




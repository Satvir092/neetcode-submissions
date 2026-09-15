class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:

            return 0
        nums.sort()

        print(nums)

        longest = 1

        maxi = 0

        last = nums[0]

        for i in range(1, len(nums)):

            if nums[i] - last < 0 or nums[i] - last > 1:

                if longest > maxi:

                    maxi = longest

                longest = 1
                last = nums[i]

            else:
                if nums[i] - last == 1:
                    longest += 1
                last = nums[i]

        if longest > maxi:

            maxi = longest

        return maxi


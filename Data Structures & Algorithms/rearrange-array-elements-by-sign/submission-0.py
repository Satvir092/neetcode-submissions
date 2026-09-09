class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        

        new = [0] * len(nums)

        l = 0
        r = 1

        for k in range(len(nums)):

            if nums[k] > 0:

                new[l] = nums[k]

                l += 2

            else:

                new[r] = nums[k]
                r += 2

        return new
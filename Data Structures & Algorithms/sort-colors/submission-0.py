class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums:

            return []

        if len(nums) == 1:

            return nums

        for i in range(1, len(nums)):

            k = i

            while k > 0 and nums[k] < nums[k - 1]:

                temp = nums[k - 1]

                nums[k - 1] = nums[k]
                nums[k] = temp
                k -= 1

        return nums
        
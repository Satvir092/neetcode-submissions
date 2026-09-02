class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0

        r = 0

        total = 0

        mini = len(nums)

        something = False

        while r < len(nums):

            total += nums[r]

            print(total)

            while total >= target:

                if r - l + 1 < mini:

                    mini = r - l + 1

                total -= nums[l]

                l += 1

                something = True

            r += 1


        if something:

            return mini

        else:

            return 0

        



            


         


        
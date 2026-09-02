class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []

        nums.sort()

        for i in range(len(nums) - 2):

            l = i + 1

            r = len(nums) - 1

            while l < r:

                if nums[i] + nums[l] + nums[r] == 0 and [nums[i], nums[l], nums[r]] not in output:

                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                elif nums[i] + nums[l] + nums[r] < 0:

                    l += 1

                else:

                    r -= 1

        return output


            
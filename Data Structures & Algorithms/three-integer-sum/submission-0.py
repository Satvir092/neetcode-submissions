class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        visited = set()

        output = []

        nums.sort()

        for i in range(len(nums) - 2):

            l = i + 1

            r = len(nums) - 1

            while l < r:

                if nums[i] + nums[l] + nums[r] == 0 and tuple(sorted([nums[i], nums[l], nums[r]])) not in visited:

                    visited.add(tuple(sorted([nums[i], nums[l], nums[r]])))

                    output.append([nums[i], nums[l], nums[r]])

                elif nums[i] + nums[l] + nums[r] < 0:

                    l += 1

                else:

                    r -= 1

        return output


            
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        import heapq

        heapq.heapify_max(nums)


        for i in range(k):

            if i == k - 1:

                return heapq.heappop_max(nums)

            heapq.heappop_max(nums)
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapify(nums)
        while len(nums) > 0 and nums[0] < k:
            first = heappop(nums)
            second = heappop(nums)
            heappush(nums, first*2+second)
            count += 1
        return count

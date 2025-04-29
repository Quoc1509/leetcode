class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = deque()
        maxQ = deque()
        l, res = 0, 0
        for r in range(len(nums)):
            while minQ and minQ[-1] > nums[r]:
                minQ.pop()
            minQ.append(nums[r])
            while maxQ and maxQ[-1] < nums[r]:
                maxQ.pop()
            maxQ.append(nums[r])
            while maxQ and minQ and maxQ[0] - minQ[0] > limit:
                if maxQ[0] == nums[l]:
                    maxQ.popleft()
                if minQ[0] == nums[l]:
                    minQ.popleft()
                l += 1
            res = max(res, r-l+1)
        return res

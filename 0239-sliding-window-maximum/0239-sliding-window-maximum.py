class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()

            queue.append(nums[i])
        res.append(queue[0])
        l = 0
        for r in range(k, len(nums)):
            if queue[0] == nums[l]:
                queue.popleft()
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])
            l += 1
            res.append(queue[0])
        return res

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res = -inf
        q = deque()
        count = 0
        for i in range(len(nums)):
            # print(q)
            while q and i - q[0][0] > k:
                q.popleft()
            if not q or q[0][1] < 0:
                count = nums[i]
            else:
                count = q[0][1] + nums[i]
            res = max(res, count)
            while q and q[-1][1] <= count:
                q.pop()
            q.append((i, count))
        return res
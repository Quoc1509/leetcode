class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        res = nums[0]
        q = deque()
        q.append((0, res))
        for i in range(1, len(nums)):
  
            while q and i-q[0][0] > k:
                q.popleft()
     
            res = q[0][1] + nums[i]
            while q and q[-1][1] < res:
                q.pop()
            q.append((i, res))
        return res
                    
        
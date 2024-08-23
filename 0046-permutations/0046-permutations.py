class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        
        def backTracking(path, mask):
            if mask == (1<<N)-1:
                res.append(path)
                return
            for i in range(N):
                if (1 << i) & mask:
                    continue
                backTracking(path + [nums[i]], mask | (1 << i))
        backTracking([], 0)
        return res

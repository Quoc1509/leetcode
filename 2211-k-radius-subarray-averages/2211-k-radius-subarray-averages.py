class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        total = sum(nums[:2*k+1])
        
        for i in range(k, len(nums)-k):
            print(total)
            res[i] = floor(total/(2*k+1))
            if i + k + 1 < len(nums):
                total += nums[i+k+1]
            total -= nums[i-k]
        return res
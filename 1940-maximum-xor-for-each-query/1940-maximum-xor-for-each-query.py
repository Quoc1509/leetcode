class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        maxNum = (2**maximumBit)-1
        count = 0
        N = len(nums)
        res = [0] * N
        for i in range(N):
            count ^= nums[i]
            res[N-i-1] = count^maxNum
            
        return res
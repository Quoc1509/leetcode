class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        bit = xor&(-xor)
        n = 0
        for num in nums:
            if num & bit:
                n ^= num
        return [n, xor^n]
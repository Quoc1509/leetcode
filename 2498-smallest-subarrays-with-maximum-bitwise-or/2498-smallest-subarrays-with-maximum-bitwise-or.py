class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        bit = [0] * 32
        res = [0] * len(nums)

        def sumOr(nums):
            i = len(bit) - 1
            while nums > 0:
                tmp = nums % 2
                nums //= 2
                bit[i] += tmp
                i -= 1

        def sumUnOr(nums):
            i = len(bit) - 1
            while nums > 0:
                tmp = nums % 2
                nums //= 2
                bit[i] -= tmp
                i -= 1

        def biToInt():
            s = 0
            for i in range(len(bit) - 1, -1, -1):
                if bit[i] > 0:
                    s += pow(2, len(bit) - 1 - i)
            return s
        
        r = len(nums)-1
        total = 0
        for l in range(len(nums)-1, -1, -1):
            total |= nums[l]
            sumOr(nums[l])
            while r > l:
                sumUnOr(nums[r])
                if total == biToInt():

                    r -= 1
                else: 
                    sumOr(nums[r])
                    break
            res[l] = (r-l+1)
        return res



        
        
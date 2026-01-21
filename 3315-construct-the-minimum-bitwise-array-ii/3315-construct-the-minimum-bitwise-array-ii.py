class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 2:
                continue
            temp = [0] * 33
            num = nums[i]
            j = 0
            while num > 0:
                temp[j] = (num&1)
                num = num >> 1
                j += 1
            for k in range(33):
                if temp[k] == 0:
                    temp[k-1] = 0
                    break
            s = "".join(map(str, reversed(temp)))
            decimal = int(s, 2)
            res[i] = decimal
        return res      

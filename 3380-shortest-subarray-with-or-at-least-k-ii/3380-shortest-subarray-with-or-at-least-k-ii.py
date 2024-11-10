class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0: return 1
        l = 0
        res = inf
        bits = [0] * 32
        def OR(num):
            temp = bin(num)[2:]
            for i in range(len(temp)):   
                bits[32-i-1] += int(temp[len(temp)-i-1])

        def bitToInt():
            temp = ''
            for i in range(31, -1, -1):
                if bits[i] > 0:
                    temp = '1' + temp
                else:
                    temp = '0' + temp
            return int(temp, 2)

        def UnOR(num):
            temp = bin(num)[2:]
            for i in range(len(temp)):
                bits[32-i-1] -= int(temp[len(temp)-i-1])

        for r in range(len(nums)):
            OR(nums[r])
            while bitToInt() >= k:
                
                res = min(res, r-l+1)
                
                UnOR(nums[l])
                l += 1
        return res if res != inf else -1
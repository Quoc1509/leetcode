class Solution:
    def subsequenceCount(self, nums: List[int]) -> int:
        #dpOdd[i]: numbers of sequence Odd sum for dpO[:i]
        #dpEven[i]: numbers of sequence Even sum for dpE[:i]
        # dpO = [0] * (len(nums)+1)
        # dpE = [0] * (len(nums)+1)
        dpO = 0
        dpE = 0
        mod = (10**9+7)
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                newDpO = dpE + dpO + 1
                newDpE = dpE + dpO
            else:
                newDpO = 2*dpO
                newDpE = 2*dpE + 1
            dpO = newDpO % mod
            dpE = newDpE % mod
        # print(dpO, dpE)
        return dpO 
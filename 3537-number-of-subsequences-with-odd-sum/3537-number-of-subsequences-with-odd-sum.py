class Solution:
    def subsequenceCount(self, nums: List[int]) -> int:
        #dpOdd[i]: numbers of sequence Odd sum for dpO[:i]
        #dpEven[i]: numbers of sequence Even sum for dpE[:i]
        # dpO = [0] * (len(nums)+1)
        # dpE = [0] * (len(nums)+1)
        dpO = 0
        dpE = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                newDpO = dpE + dpO + 1
                newDpE = dpE + dpO
            else:
                newDpO = dpO + dpE + 1 if dpO > 0 else 0
                newDpE = 2*dpE + 1
            dpO = newDpO
            dpE = newDpE
        # print(dpO, dpE)
        return dpO % (10**9+7)
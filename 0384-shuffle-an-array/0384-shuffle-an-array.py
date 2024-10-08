class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        return self.arr

    def shuffle(self) -> List[int]:
        res = self.arr.copy()
        for i in range(len(self.arr)):
            ind = random.randint(i, len(self.arr)-1)
            res[i], res[ind] = res[ind], res[i]
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
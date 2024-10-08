class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums

    def reset(self) -> List[int]:
        return self.arr

    def shuffle(self) -> List[int]:
        temp = set()
        res = []
        while len(temp) != len(self.arr):
            ind = random.randint(0, len(self.arr)-1)
            if ind not in temp:
                temp.add(ind)
                res.append(self.arr[ind])
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
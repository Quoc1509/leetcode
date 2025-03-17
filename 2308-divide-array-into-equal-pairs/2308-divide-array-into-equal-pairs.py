class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for key, item in count.items():
            if item % 2 == 1:
                return False
        return True
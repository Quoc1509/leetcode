class Compare(int):
    def __lt__(a, b):
        a = str(a)
        b = str(b)
        if a+b > b+a:
            return True
        else:
            return False


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = sorted(nums, key=Compare)
        res = [str(i) for i in res]
        return str(int(''.join(res)))
            
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        temp = set(nums)
        # res = ['']
        @cache
        def BT(s):
            if len(s) == len(nums[0]):
                if s not in nums:
                    return s
            if len(s) > len(nums[0]):
                return None
            return BT(s+'1') or BT(s+'0')

        res = BT('')
        print(res)
        return res
        
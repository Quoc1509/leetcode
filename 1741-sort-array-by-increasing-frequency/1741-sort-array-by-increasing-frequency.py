class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        temp = []
        for key, item in count.items():
            temp.append((item, key))
        temp.sort(key = lambda x:[x[0], -x[1]])
        res = []
        for a, b in temp:
            res.extend([b]*a)
        return res
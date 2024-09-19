class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        temp = [[] for _ in range(len(nums)+1)]
        for key, item in count.items():
            temp[item].append(key)
        res = []
        for i in range(len(temp)-1, -1, -1):
            res.extend(temp[i])
            if len(res) == k:
                break
        return res
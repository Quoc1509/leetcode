class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [[] for _ in range(len(nums)+1)] 
        res = []
        for key, item in count.items():
            arr[item].append(key)
        for sub in arr[::-1]:
            res.extend(sub)
            if len(res) == k:
                return res
        return []
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hashMap = defaultdict(list)
        res = [0] * len(nums)
        for i, e in enumerate(nums):
            hashMap[e].append(i)

        for key, item in hashMap.items():
            if len(item) == 1: continue
            prefix = [0] * (len(item)+1)
            for i in range(len(item)):
                prefix[i+1] = prefix[i] + item[i]
            for i in range(len(item)):
                left = item[i] * i - prefix[i]
                right = (prefix[-1] - prefix[i+1]) - item[i] * (len(item)-i-1) 
                count = left + right
                res[item[i]] = count
        return res


        
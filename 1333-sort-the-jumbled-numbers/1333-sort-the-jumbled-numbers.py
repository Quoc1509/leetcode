class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):
            if num == 0: return mapping[0]
            res = 0
            i = 0
            while num > 0:
                temp = num % 10
                num //= 10
                res = ((pow(10, i) * mapping[temp]) + res)
                i += 1
            return res
        ans = defaultdict(list)
        for i in nums:
            c = convert(i)
            ans[c].append(i)
        # ans.sort()
        temp = []
        for key, item in ans.items():
            temp.append((key, item))
        temp.sort()
        r = []
        for a, b in temp:
            r.extend(b)
        return r
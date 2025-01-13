class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        res = len(s)
        for key, item in count.items():
            while item > 2:
                item -= 2
                res -= 2
        # print(res)
        return res
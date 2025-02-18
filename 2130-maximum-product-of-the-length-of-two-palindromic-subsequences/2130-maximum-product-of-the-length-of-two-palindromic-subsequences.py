class Solution:
    def maxProduct(self, s: str) -> int:
        res = [0]
        @cache
        def BT(s1, s2, i):
            # print(i, s1, s2)
            if s1 == s1[::-1] and s2 == s2[::-1]:
                res[0] = max(res[0], len(s1)*len(s2))
            if i >= len(s):
                return
            return BT(s1+s[i], s2, i+1) or BT(s1, s2+s[i], i+1) or BT(s1, s2, i+1)
        BT('', '', 0)
        # print(res)
        return res[0]
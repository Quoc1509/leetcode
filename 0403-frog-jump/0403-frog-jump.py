class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] > 1: return False
        mp = {}
        for i in range(len(stones)):
            mp[stones[i]] = i

        @cache
        def dp(i, k):
            if i >= len(stones)-1:
                return True
            one = two = three = False
            if stones[i] + k - 1 in mp and stones[i] + k - 1 > stones[i]:
                one = dp(mp[stones[i] + k - 1], stones[mp[stones[i] + k - 1]] - stones[i])
            if stones[i] + k in mp:
                two = dp(mp[stones[i] + k], stones[mp[stones[i] + k]] - stones[i])
            if stones[i] + k + 1 in mp:
                three = dp(mp[stones[i] + k + 1], stones[mp[stones[i] + k + 1]] - stones[i])
            return one or two or three
        return dp(1, 1)
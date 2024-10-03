class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word = set(wordDict)
        memo = {}
        def backTracking(i):
            if i == len(s):
                return ['']
            if i in memo: return memo[i]
            res = []
            cur = ''
            for j in range(i, len(s)):
                cur += s[j]
                if cur in word:
                    temp = backTracking(j+1)
                    for t in temp:
                        a = cur + (' ' + t if t else '')
                        res.append(a)
            memo[i] = res
            return memo[i]
        return backTracking(0)

                
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        listWord = set(words)
        # words.sort(key = lambda x: len(x), reverse = True)
        temp = ['']
        res = []
        memo = {}
        def DP(i):
            if i in memo: return memo[i]
            if i >= len(temp[0]):
                # print(temp[0])
                return 0
            res = -inf
            for j in range(i, len(temp[0])):
                if temp[0][i:j+1] in listWord:
                    res = max(res, DP(j+1)+1)
            memo[i] = res
            return memo[i]

        for word in words:
            memo = {}
            temp[0] = word
            if DP(0) > 1:
                res.append(word)
        return res
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        listWord = set(words)
        # words.sort(key = lambda x: len(x), reverse = True)
        temp = ['']
        res = []
        memo = {}
        def DP(i, w):
            if i in memo: return memo[i]
            if i >= len(w):
                # print(temp[0])
                return 0
            res = -inf
            for j in range(i, len(w)):
                if w[i:j+1] in listWord:
                    res = max(res, DP(j+1, w)+1)
            memo[i] = res
            return memo[i]

        for word in words:
            memo = {}
            # temp[0] = word
            if DP(0, word) > 1:
                res.append(word)
        return res
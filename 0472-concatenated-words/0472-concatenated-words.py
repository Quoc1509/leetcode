class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        listWord = set()
        words.sort(key = lambda x: len(x))
        memp = {}
        res = []
        def DP(i, word):
            if i in memo:
                return memo[i]
            if i >= len(word):
                return True
            for j in range(i, len(word)):
                if word[i: j+1] in listWord:
                    if DP(j+1, word):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return memo[i]


        for word in words:
            memo = {}
            if DP(0, word):
                res.append(word)
            listWord.add(word)
        return res
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            l = len(words[i])
            for j in range(i+1, len(words)):
                if len(words[j]) < l:
                    continue
                if words[j][:l] == words[i] and words[j][-l:] == words[i]:
                    res += 1
        return res
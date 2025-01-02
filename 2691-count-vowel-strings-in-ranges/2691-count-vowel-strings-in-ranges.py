class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vol = {'a', 'e', 'i', 'o', 'u'}
        N = len(words)
        prefix = [0] * (N+1)
        for i in range(len(words)):
            if words[i][0] in vol and words[i][-1] in vol:
                prefix[i+1] = prefix[i]+1
            else:
                prefix[i+1] = prefix[i]
        res = [0] * len(queries)
        # print(prefix)
        for i in range(len(queries)):
            a, b = queries[i]
            # if a == b:
            #     res[i] = (1 if words[a][0] in vol and words[a][-1] in vol else 0)
            # else:
            res[i] = prefix[b+1]-prefix[a]
        return res
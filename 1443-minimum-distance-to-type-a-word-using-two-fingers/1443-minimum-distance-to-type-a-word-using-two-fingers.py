class Solution:
    def minimumDistance(self, word: str) -> int:
        alpha = 65
        lenRow = 6
        r = c = 0
        mapDict = {}
        for i in range(26):
            c = i % 6
            r = i // 6
            mapDict[chr(alpha+i)] = (r, c)
            
        @cache
        def BT(i, fin1, fin2):
            if i == len(word):
                return 0

            res1 = BT(i+1, mapDict[word[i]], fin2) + ((abs(fin1[0]-mapDict[word[i]][0]) + abs(fin1[1]-mapDict[word[i]][1])) if fin1[0] != -1 and fin1[1] != -1 else 0)
            res2 = BT(i+1, fin1, mapDict[word[i]]) + ((abs(fin2[0]-mapDict[word[i]][0]) + abs(fin2[1]-mapDict[word[i]][1])) if fin2[0] != -1 and fin2[1] != -1 else 0)
            return min(res1, res2)
        return BT(0, (-1,-1), (-1,-1))
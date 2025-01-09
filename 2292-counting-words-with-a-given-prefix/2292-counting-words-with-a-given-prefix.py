class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0 
        l = len(pref)
        for word in words:
            if word[:l] == pref:
                res += 1
        return res
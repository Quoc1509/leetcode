class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = set(spaces)
        res = []
        l = 0
        for r in range(len(s)):
            if r in spaces:
                res.append(s[l: r])
                l = r
        res.append(s[l:])
        return ' '.join(res)

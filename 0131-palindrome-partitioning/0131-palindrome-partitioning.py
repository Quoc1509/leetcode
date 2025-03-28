class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def BT(path, i):
            if i >= len(s):
                res.append(path[:])
                return
            for idx in range(i, len(s)):
                temp = s[i:idx+1]
                if temp == temp[::-1]:
                    BT(path+[temp], idx+1)
        BT([], 0)
        return res
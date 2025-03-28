class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def BT(o, c, s):
            if o == n and c == n:
                res.append(s)
                return
            if o < n:
                BT(o+1, c, s+'(')
            if o > c:
                BT(o, c + 1, s+')')
        BT(0, 0, '')
        # print(res)
        return res
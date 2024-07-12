class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        q1 = list(s)
        q2 = []
        res = [0]
        def ab():
            for i in q1:
                if q2 and i == 'b' and q2[-1] == 'a':
                    res[0] += x
                    q2.pop()
                    continue
                q2.append(i)
             
        def ba():
            for i in q1:
                if q2 and i == 'a' and q2[-1] == 'b':
                    res[0] += y
                    q2.pop()
                    continue
                q2.append(i)

        if x > y:
            ab()
            q1 = q2.copy()
            # print(q2)
            q2 = []
            ba()
        else:
            ba()
            q1 = q2.copy()
            # print(q2)
            q2 = []
            ab()
        return res[0]
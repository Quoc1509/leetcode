from sortedcontainers import SortedList
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        temp = []
        count = Counter(s)
        for key, item in count.items():
            temp.append([key, item])
        temp = SortedList(temp)
        res = ''
        while temp:
            a, b = temp[-1]
            if res and a == res[-1]:
                if len(temp) == 1:
                    break
                else:
                    res += temp[-2][0]
                    temp[-2][1] -= 1
                    if temp[-2][1] == 0:
                        temp.remove(temp[-2])
            else:
                if b > repeatLimit:
                    res += (a*repeatLimit)
                    temp[-1][1] -= repeatLimit
                else:
                    res += (a*b)
                    temp.remove([a,  b])

        return res
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1, m])
        vFences.extend([1, n])
        hFences.sort()
        vFences.sort()
        temp = set()

        for i in range(len(hFences)):
            for j in range(i-1, -1, -1):
                temp.add(hFences[i]-hFences[j])
        res = -1
        for i in range(len(vFences)):
            for j in range(i-1, -1, -1):
                length = vFences[i] - vFences[j]
                if length in temp:
                    res = max(res, (length*length))
        return -1 if res == -1 else res%(10**9+7)

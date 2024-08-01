class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp = []
        for i in range(len(names)):
            temp.append([heights[i], names[i]])
        temp.sort(reverse=True)
        res = []
        for h, n in temp:
            res.append(n)
        return res
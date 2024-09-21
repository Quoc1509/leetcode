class Solution:
    def minSwaps(self, data: List[int]) -> int:
        one = 0
        for i in data:
            if i == 1:
                one += 1
        if one < 2: return 0
        print(one)
        res = 0
        for i in range(one):
            if data[i] == 0:
                res += 1
        if res == 0: return 0
        temp = res
        j = 0
        for i in range(one, len(data)):
            if data[i] == 0:
                temp += 1
            if data[j] == 0:
                temp -= 1
            res = min(res, temp)
            j += 1
        return res
